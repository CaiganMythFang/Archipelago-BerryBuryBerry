from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BerryBuryBerryWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: BerryBuryBerryWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BerryBuryBerryWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    upgrade_screen = Region("Upgrade Screen", world.player, world.multiworld)
    zone_1 = Region("Zone 1", world.player, world.multiworld)
    zone_2 = Region("Zone 2", world.player, world.multiworld)
    zone_3 = Region("Zone 3", world.player, world.multiworld)
    zone_4 = Region("Zone 4", world.player, world.multiworld)
    zone_5 = Region("Zone 5", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [upgrade_screen, zone_1, zone_2, zone_3, zone_4, zone_5]

    # # Some regions may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
        # top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
        # regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: BerryBuryBerryWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    upgrade_screen = world.get_region("Upgrade Screen")
    zone_1 = world.get_region("Zone 1")
    zone_2 = world.get_region("Zone 2")
    zone_3 = world.get_region("Zone 3")
    zone_4 = world.get_region("Zone 4")
    zone_5 = world.get_region("Zone 5")

    # # Okay, now we can get connecting. For this, we need to create Entrances.
    # # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # # One way to create an Entrance is by calling the Entrance constructor.
    # overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    # overworld.exits.append(overworld_to_bottom_right_room)

    # # You can then connect the Entrance to the target region.
    # overworld_to_bottom_right_room.connect(bottom_right_room)

    # # An even easier way is to use the region.connect helper.
    # overworld.connect(right_room, "Overworld to Right Room")
    # right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # # The region.connect helper even allows adding a rule immediately.
    # # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    upgrade_screen.connect(zone_1, "Upgrade Screen to Zone 1")
    zone_1.connect(zone_2, "Zone 1 to Zone 2")
    zone_2.connect(zone_3, "Zone 2 to Zone 3")
    zone_3.connect(zone_4, "Zone 3 to Zone 4")
    zone_4.connect(zone_5, "Zone 4 to Zone 5")

    # # Some Entrances may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
        # top_middle_room = world.get_region("Top Middle Room")
        # overworld.connect(top_middle_room, "Overworld to Top Middle Room")
