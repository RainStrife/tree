import json
from collections import defaultdict
from django.shortcuts import render
from core.models import Material, Building


def get_tree(request):
    materials = defaultdict(lambda: [])
    buildings = defaultdict(lambda: [])
    available_materials = list(Material.objects.filter(buildings_can_produce__isnull=True))

    materials['0'] = list(Material.objects.filter(buildings_can_produce__isnull=True))

    buildings['0'] = list(Building.objects.filter(materials_for_build__isnull=True))

    for i in range(1, 100):

        if buildings[str(i-1)]:
            for building in buildings[str(i-1)]:
                for material in building.materials_produce.all():
                    materials[str(i)].append(material)
                    available_materials.append(material)
                for material in materials[str(i)]:
                    for building in material.buildings_can_be_build.all():
                        flag = True
                        for material in building.materials_for_build.all():
                            if material in available_materials:
                                pass
                            else:
                                flag = False
                                break
                        if flag:
                            buildings[str(i)].append(building)
            i += 1
        else:
            break

    context = {
        'materials': list(sorted(materials.items())),
        'buildings': list(sorted(buildings.items())),
    }

    return render(request, 'core/tree.html', context)


def get_graph(request):
    graph = []

    for building in Building.objects.all():
        graph.append(
            {'data': {
                'id': building.name,
                'color': 'red'
                      }
             }
        )

    for material in Material.objects.filter(buildings_can_produce__isnull=True, buildings_can_be_build=True):
        graph.append(
            {'data': {
                'id': material.name,
                'color': 'yellow'
            }
            }
        )

    for building in Building.objects.all():
        for material in building.materials_produce.all():
            for target_building in material.buildings_can_be_build.all():
                graph.append(
                    {
                        'data': {
                            'id': str(building.name) + '_' + str(target_building.name),
                            'source': building.name,
                            'target': target_building.name,
                            'name': material.name
                        }
                    }
                )
    for material in Material.objects.filter(buildings_can_produce__isnull=True):
        for building in material.buildings_can_be_build.all():
            graph.append(
                {
                    'data': {
                        'id': str(material.name) + '_' + str(building.name),
                        'source': material.name,
                        'target': building.name,
                        'name': ''
                    }
                }
            )

    for material in Material.objects.filter(buildings_can_be_build__isnull=True):
        if material.buildings_can_produce.all():
            graph.append(
                {'data': {
                    'id': material.name,
                    'color': 'grey'
                }
                }
            )
            for building in material.buildings_can_produce.all():
                graph.append(
                    {
                        'data': {
                            'id': str(material.name) + '_' + str(building.name),
                            'target': material.name,
                            'source': building.name,
                            'name': ''
                        }
                    }
                )
        else:
            graph.append(
                {'data': {
                    'id': material.name,
                    'color': 'pink'
                }
                }
            )

    print(graph)
    context = {
        'graph': json.dumps(graph),
    }
    return render(request, 'core/graph.html', context)
