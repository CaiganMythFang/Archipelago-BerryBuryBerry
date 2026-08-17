from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BerryBuryBerryWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.

# Every location you want to have, whether or not its obtainable depending on the settings you set up, must be referenced here with a unique String name, with a unique ID integer.
LOCATION_NAME_TO_ID = {
    "Shop Berry Buddy 1": 1, # 1
    "Shop Berry Buddy 2": 2, # 15
    "Shop Berry Buddy 3": 3, # 100
    "Shop Berry Buddy 4": 4, # 1,000
    "Shop Berry Buddy 5": 5, # 10,000
    "Shop Berry Buddy 6": 6, # 100,000
    "Shop Berry Buddy 7": 7, # 1,000,000
    "Shop Sledgehammer 1": 8, # 125
    "Shop Sledgehammer 2": 9, # 10,000
    "Shop Sledgehammer 3": 10, # 150,000
    "Shop Sledgehammer 4": 11, # 1,000,000
    "Shop Movable Hole": 12, # 50
    "Shop Hole Range 1": 13, # 150
    "Shop Hole Range 2": 14, # 550
    "Shop Hole Range 3": 15, # 10,000
    "Shop Hole Range 4": 16, # 40,000
    "Shop Hole Range 5": 17, # 200,000
    "Shop Hole Range 6": 18, # 500,000
    "Shop Hole Range 7": 19, # 1,500,000
    "Shop Hole Range 8": 20, # 6,000,000
    "Shop Hole Speed 1": 21, # 10,000
    "Shop Hole Speed 2": 22, # 750,000
    "Shop Vaccuum": 23, # 25
    "Shop Vaccuum Capacity 1": 24, # 1,500
    "Shop Vaccuum Capacity 2": 25, # 10,000
    "Shop Vaccuum Capacity 3": 26, # 50,000
    "Shop Vaccuum Capacity 4": 27, # 100,000
    "Shop Vaccuum Capacity 5": 28, # 300,000
    "Shop Vaccuum Capacity 6": 29, # 600,000
    "Shop Vaccuum Capacity 7": 30, # 1,200,000
    "Shop Vaccuum Capacity 8": 31, # 2,400,000
    "Shop Vaccuum Capacity 9": 32, # 4,800,000
    "Shop Vaccuum Capacity 10": 33, # 10,000,000
    "Shop Auto Pickup Coins": 34, # 500
    "Shop Auto Pickup Range 1": 35, # 2,500
    "Shop Auto Pickup Range 2": 36, # 25,000
    "Shop Auto Pickup Range 3": 37, # 100,000
    "Shop Auto Pickup Range 4": 38, # 1,000,000
    "Shop Chainsaw": 39, # 75,000
    "Shop JUICED Multiplier 1": 40, # 250,000
    "Shop JUICED Multiplier 2": 41, # 1,250,000
    "Shop JUICED Multiplier 3": 42, # 15,000,000
    "Shop JUICED Multiplier 4": 43, # 75,000,000
    "Shop Increase Day Length 1": 44, # 250
    "Shop Increase Day Length 2": 45, # 1,200
    "Shop Increase Day Length 3": 46, # 4,000
    "Shop Increase Day Length 4": 47, # 16,000
    "Shop Increase Day Length 5": 48, # 64,000
    "Shop Increase Day Length 6": 49, # 256,000
    "Shop Increase Day Length 7": 50, # 1,024,000
    "Shop Increase Day Length 8": 51, # 65,000,000
    "Shop Flower to Bush": 52, # 50,000
    "Shop Bush to Tree": 53, # 1,500,000
    "Shop Golden Berry Chance 1": 54, # 50,000
    "Shop Golden Berry Chance 2": 55, # 500,000
    "Shop Golden Berry Chance 3": 56, # 5,000,000
    "Shop Golden Berry Chance 4": 57, # 150,000,000
    "Shop Golden Berry Multiplier 1": 58, # 60,000
    "Shop Golden Berry Multiplier 2": 59, # 180,000
    "Shop Golden Berry Multiplier 3": 60, # 540,000
    "Shop Golden Berry Multiplier 4": 61, # 1,650,000
    "Shop Golden Berry Multiplier 5": 62, # 60,000,000
    "Shop Berry Blitz": 63, # 250
    "Shop Berry Blitz Duration 1": 64, # 1,500
    "Shop Berry Blitz Duration 2": 65, # 15,000
    "Shop Berry Blitz Duration 3": 66, # 250,000
    "Shop Berry Blitz Duration 4": 67, # 1,000,000
    "Shop Berry Blitz Duration 5": 68, # 48,000,000
    "Shop Berry Blitz Bonus Growth 1": 69, # 2,500
    "Shop Berry Blitz Bonus Growth 2": 70, # 100,000
    "Shop Berry Blitz Bonus Growth 3": 71, # 1,000,000
    "Shop Berry Blitz Bonus Growth 4": 72, # 50,000,000
    "Shop Berry Fountain Ability": 73, # 2,000
    "Shop Berry Fountain Cooldown 1": 74, # 25,000
    "Shop Berry Fountain Cooldown 2": 75, # 100,000
    "Shop Berry Fountain Cooldown 3": 76, # 500,000
    "Shop Berry Fountain Cooldown 4": 77, # 2,000,000
    "Shop Berry Fountain Cooldown 5": 78, # 50,000,000
    "Shop Star Wand": 79, # 30
    "Shop PopGun": 80, # 8,500
    "Shop Berry Chooser": 81, # 300,000
    "Shop Trampoline": 82, # 250,000
    "Shop Star Orb Generator": 83, # 10
    "Shop Auto Star Orb Popper": 84, # 90,000
    "Shop Bibble": 85, # 20,000
    "Shop Star Key": 86, # 5,000,000
    "Shop Rewind 1": 87, # 10,000
    "Shop Rewind 2": 88, # 50,000
    "Shop Rewind 3": 89, # 200,000
    "Shop Rewind 4": 90, # 500,000
    "Shop Rewind 5": 91, # 1,000,000
    "Shop Rewind 6": 92, # 2,000,000
    "Shop Rewind 7": 93,
    "Shop Rewind 8": 94,
    "5 Gnomes": 95,
    "25 Gnomes": 96,
    "50 Gnomes": 97,
    "75 Gnomes": 98,
    "100 Gnomes": 99,
    "5 Props": 100,
    "25 Props": 101,
    "50 Props": 102,
    "75 Props": 103,
    "100 Props": 104,
    "250 Props": 105,
    "500 Props": 106,
    "750 Props": 107,
    "1,000 Props": 108,
    "10 Coins": 109,
    "25 Coins": 110,
    "100 Coins": 111,
    "250 Coins": 112,
    "500 Coins": 113,
    "1,000 Coins": 114,
    "2,500 Coins": 115,
    "5,000 Coins": 116,
    "10,000 Coins": 117,
    "25,000 Coins": 118,
    "50,000 Coins": 119,
    "100,000 Coins": 120,
    "250,000 Coins": 121,
    "500,000 Coins": 122,
    "1,000,000 Coins": 123,
    "2,000,000 Coins": 124,
    "10,000,000 Coins": 125,
    "25,000,000 Coins": 126,
    "50,000,000 Coins": 127,
    "10 Stars": 128,
    "25 Stars": 129,
    "50 Stars": 130,
    "100 Stars": 131,
    "250 Stars": 132,
    "500 Stars": 133,
    "1,000 Stars": 134,
    "2,500 Stars": 135,
    "5,000 Stars": 136,
    "9,999 Stars": 137,
    "Break 1 Wall": 138,
    "Break 2 Walls": 139,
    "Break 5 Walls": 140,
    "Break 10 Walls": 141,
    "Break 20 Walls": 142,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class BerryBuryBerryLocation(Location):
    game = "BeryBurryBerry"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BerryBuryBerryWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BerryBuryBerryWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    
    # We start by defining our regions.
    upgrade_screen = world.get_region("Upgrade Screen")
    zone_1 = world.get_region("Zone 1")
    zone_2 = world.get_region("Zone 2")
    zone_3 = world.get_region("Zone 3")
    zone_4 = world.get_region("Zone 4")
    zone_5 = world.get_region("Zone 5")

    # # One way to create locations is by just creating them directly via their constructor.
    # bottom_left_chest = APQuestLocation(
        # world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    # )

    # # You can then add them to the region.
    # overworld.locations.append(bottom_left_chest)

    # # A simpler way to do this is by using the region.add_locations helper.
    # # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # # You also need to pass your overridden Location class.
    # bottom_right_room_locations = get_location_names_with_ids(
        # ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    # )
    # bottom_right_room.add_locations(bottom_right_room_locations, APQuestLocation)

    # top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    # top_left_room.add_locations(top_left_room_locations, APQuestLocation)
    
    # Now we put each location we listed above in one of the regions.
    
    # Start by defining the list of locations in a region by strings. get_location_names_with_ids() uses the string to pull the appropriate ID integer for it, so it is important that both the name here is accurate, and that the ID integer you set above is unique.
    upgrade_screen_locations = get_location_names_with_ids(
        ["Shop Berry Buddy 1", "Shop Berry Buddy 2", "Shop Berry Buddy 3", "Shop Berry Buddy 4", "Shop Berry Buddy 5", "Shop Berry Buddy 6", "Shop Berry Buddy 7", "Shop Sledgehammer 1", "Shop Sledgehammer 2", "Shop Sledgehammer 3", "Shop Sledgehammer 4", "Shop Movable Hole", "Shop Hole Range 1", "Shop Hole Range 2", "Shop Hole Range 3", "Shop Hole Range 4", "Shop Hole Range 5", "Shop Hole Range 6", "Shop Hole Range 7", "Shop Hole Range 8", "Shop Hole Speed 1", "Shop Hole Speed 2", "Shop Vaccuum", "Shop Vaccuum Capacity 1", "Shop Vaccuum Capacity 2", "Shop Vaccuum Capacity 3", "Shop Vaccuum Capacity 4", "Shop Vaccuum Capacity 5", "Shop Vaccuum Capacity 6", "Shop Vaccuum Capacity 7", "Shop Vaccuum Capacity 8", "Shop Vaccuum Capacity 9", "Shop Vaccuum Capacity 10", "Shop Auto Pickup Coins", "Shop Auto Pickup Range 1", "Shop Auto Pickup Range 2", "Shop Auto Pickup Range 3", "Shop Auto Pickup Range 4", "Shop Chainsaw", "Shop JUICED Multiplier 1", "Shop JUICED Multiplier 2", "Shop JUICED Multiplier 3", "Shop JUICED Multiplier 4", "Shop Increase Day Length 1", "Shop Increase Day Length 2", "Shop Increase Day Length 3", "Shop Increase Day Length 4", "Shop Increase Day Length 5", "Shop Increase Day Length 6", "Shop Increase Day Length 7", "Shop Increase Day Length 8", "Shop Flower to Bush", "Shop Bush to Tree", "Shop Golden Berry Chance 1", "Shop Golden Berry Chance 2", "Shop Golden Berry Chance 3", "Shop Golden Berry Chance 4", "Shop Golden Berry Multiplier 1", "Shop Golden Berry Multiplier 2", "Shop Golden Berry Multiplier 3", "Shop Golden Berry Multiplier 4", "Shop Golden Berry Multiplier 5", "Shop Berry Blitz", "Shop Berry Blitz Duration 1", "Shop Berry Blitz Duration 2", "Shop Berry Blitz Duration 3", "Shop Berry Blitz Duration 4", "Shop Berry Blitz Duration 5", "Shop Berry Blitz Bonus Growth 1", "Shop Berry Blitz Bonus Growth 2", "Shop Berry Blitz Bonus Growth 3", "Shop Berry Blitz Bonus Growth 4", "Shop Berry Fountain Ability", "Shop Berry Fountain Cooldown 1", "Shop Berry Fountain Cooldown 2", "Shop Berry Fountain Cooldown 3", "Shop Berry Fountain Cooldown 4", "Shop Berry Fountain Cooldown 5", "Shop Star Wand", "Shop PopGun", "Shop Berry Chooser", "Shop Trampoline", "Shop Star Orb Generator", "Shop Auto Star Orb Popper", "Shop Bibble", "Shop Star Key", "Shop Rewind 1", "Shop Rewind 2", "Shop Rewind 3", "Shop Rewind 4", "Shop Rewind 5", "Shop Rewind 6", "Shop Rewind 7", "Shop Rewind 8",]
    )
    upgrade_screen.add_locations(upgrade_screen_locations, BerryBuryBerryLocation)
    zone_1_locations = get_location_names_with_ids(
        ["5 Gnomes", "5 Props", "25 Props", "10 Coins", "25 Coins", "100 Coins", "250 Coins", "500 Coins", "1,000 Coins", "10 Stars", "25 Stars", "Break 1 Wall", "Break 2 Walls", "Break 5 Walls", "Break 10 Walls", "Break 20 Walls"]
    )
    zone_1.add_locations(zone_1_locations, BerryBuryBerryLocation)
    
    zone_2_locations = get_location_names_with_ids(
        ["25 Gnomes", "50 Props", "75 Props", "100 Props", "2,500 Coins", "5,000 Coins", "10,000 Coins", "25,000 Coins", "50,000 Coins", "50 Stars", "100 Stars"]
    )
    zone_2.add_locations(zone_2_locations, BerryBuryBerryLocation)
    
    zone_3_locations = get_location_names_with_ids(
        ["50 Gnomes", "250 Props", "100,000 Coins", "250 Stars", "500 Stars"]
    )
    zone_3.add_locations(zone_3_locations, BerryBuryBerryLocation)
    
    zone_4_locations = get_location_names_with_ids(
        ["75 Gnomes", "500 Props", "750 Props", "250,000 Coins", "500,000 Coins", "1,000 Stars", "2,500 Stars"]
    )
    zone_4.add_locations(zone_4_locations, BerryBuryBerryLocation)
    
    zone_5_locations = get_location_names_with_ids(
        ["100 Gnomes", "1,000 Props", "1,000,000 Coins", "2,000,000 Coins", "10,000,000 Coins", "25,000,000 Coins", "50,000,000 Coins", "5,000 Stars", "9,999 Stars"]
    )
    zone_5.add_locations(zone_5_locations, BerryBuryBerryLocation)

    # # Locations may be in different regions depending on the player's options.
    # # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    # top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    # if world.options.hammer:
        # top_middle_room = world.get_region("Top Middle Room")
        # top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    # else:
        # overworld.add_locations(top_middle_room_locations, APQuestLocation)

    # # Locations may exist only if the player enables certain options.
    # # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    # if world.options.prop_sanity:
        # # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # # exist, it must still always be present in the world's location_name_to_id.
        # # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        # bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        # overworld.add_locations(bottom_left_extra_chest, BerryBuryBerryLocation)
    if world.options.prop_sanity:
        prop_sanity_zone_1_locations = get_location_names_with_ids(
        ["Speech Bubble - Basic Controls", "Speech Bubble - Vaccuum"]
        )
        zone_1.add_locations(prop_sanity_zone_1_locations, BerryBuryBerryLocation)


def create_events(world: BerryBuryBerryWorld) -> None:
    # # # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # # # In our case, the player must press a button in the top left room to open the final boss door.
    # # # AP has something for this purpose: "Event locations" and "Event items".
    # # # An event location is no different than a regular location, except it has the address "None".
    # # # It is treated during generation like any other location, but then it is discarded.
    # # # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # # # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    # # top_left_room = world.get_region("Top Left Room")
    # # final_boss_room = world.get_region("Final Boss Room")
    
    # Start by defining each Region
    upgrade_screen = world.get_region("Upgrade Screen")
    zone_1 = world.get_region("Zone 1")
    zone_2 = world.get_region("Zone 2")
    zone_3 = world.get_region("Zone 3")
    zone_4 = world.get_region("Zone 4")
    zone_5 = world.get_region("Zone 5")

    # # # One way to create an event is simply to use one of the normal methods of creating a location.
    # # button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    # # top_left_room.locations.append(button_in_top_left_room)

    # # # We then need to put an event item onto the location.
    # # # An event item is an item whose code is "None" (same as the event location's address),
    # # # and whose classification is "progression". Item creation will be discussed more in items.py.
    # # # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # # # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # # # it is common practice to create the item when creating the location.
    # # # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # # # we'll create both the event location and the event item in our locations.py code.
    # # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    # # button_in_top_left_room.place_locked_item(button_item)

    # # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # # Luckily, we have another event we want to create: The Victory event.
    # # We will use this event to track whether the player can win the game.
    # # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    # zone_1.add_event(
        # "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    # )
    
    # Here we are setting up a location/item event pairing to match up with the Upgrade Screen. That way, we can send the location when said upgrade spot is purchased, and always receive the item paired with it.
    # These items will be used in rules.py so the system knows that higher tier Upgrade purchases will require the lower tier to be purchased first.
    upgrade_screen.add_event(
        "Purchase Berry Buddy 1", "Purchased Berry Buddy 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Berry Buddy 2", "Purchased Berry Buddy 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Berry Buddy 3", "Purchased Berry Buddy 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Berry Buddy 4", "Purchased Berry Buddy 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Berry Buddy 5", "Purchased Berry Buddy 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Berry Buddy 6", "Purchased Berry Buddy 6", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
    
    upgrade_screen.add_event(
        "Purchase Sledgehammer 1", "Purchased Sledgehammer 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Sledgehammer 2", "Purchased Sledgehammer 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Sledgehammer 3", "Purchased Sledgehammer 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Sledgehammer 4", "Purchased Sledgehammer 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Movable Hole", "Purchased Movable Hole", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 1", "Purchased Hole Range 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 2", "Purchased Hole Range 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 3", "Purchased Hole Range 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 4", "Purchased Hole Range 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 5", "Purchased Hole Range 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 6", "Purchased Hole Range 6", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 7", "Purchased Hole Range 7", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Range 8", "Purchased Hole Range 8", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Speed 1", "Purchased Hole Speed 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Hole Speed 2", "Purchased Hole Speed 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum", "Purchased Vaccuum", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 1", "Purchased Vaccuum Capacity 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 2", "Purchased Vaccuum Capacity 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 3", "Purchased Vaccuum Capacity 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 4", "Purchased Vaccuum Capacity 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 5", "Purchased Vaccuum Capacity 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 6", "Purchased Vaccuum Capacity 6", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 7", "Purchased Vaccuum Capacity 7", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 8", "Purchased Vaccuum Capacity 8", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 9", "Purchased Vaccuum Capacity 9", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Vaccuum Capacity 10", "Purchased Vaccuum Capacity 10", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Pickup Coins", "Purchased Auto Pickup Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Pickup Range 1", "Purchased Auto Pickup Range 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Pickup Range 2", "Purchased Auto Pickup Range 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Pickup Range 3", "Purchased Auto Pickup Range 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Pickup Range 4", "Purchased Auto Pickup Range 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Chainsaw", "Purchased Chainsaw", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase JUICED Multiplier 1", "Purchased JUICED Multiplier 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase JUICED Multiplier 2", "Purchased JUICED Multiplier 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase JUICED Multiplier 3", "Purchased JUICED Multiplier 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase JUICED Multiplier 4", "Purchased JUICED Multiplier 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 1", "Purchased Increase Day Length 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 2", "Purchased Increase Day Length 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 3", "Purchased Increase Day Length 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 4", "Purchased Increase Day Length 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 5", "Purchased Increase Day Length 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 6", "Purchased Increase Day Length 6", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 7", "Purchased Increase Day Length 7", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Increase Day Length 8", "Purchased Increase Day Length 8", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Flower to Bush", "Purchased Flower to Bush", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Bush to Tree", "Purchased Bush to Tree", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Chance 1", "Purchased Golden Berry Chance 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Chance 2", "Purchased Golden Berry Chance 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Chance 3", "Purchased Golden Berry Chance 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Chance 4", "Purchased Golden Berry Chance 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Multiplier 1", "Purchased Golden Berry Multiplier 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Multiplier 2", "Purchased Golden Berry Multiplier 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Multiplier 3", "Purchased Golden Berry Multiplier 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Multiplier 4", "Purchased Golden Berry Multiplier 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Golden Berry Multiplier 5", "Purchased Golden Berry Multiplier 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz", "Purchased Berry Blitz", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Duration 1", "Purchased Berry Blitz Duration 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Duration 2", "Purchased Berry Blitz Duration 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Duration 3", "Purchased Berry Blitz Duration 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Duration 4", "Purchased Berry Blitz Duration 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Duration 5", "Purchased Berry Blitz Duration 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Bonus Growth 1", "Purchased Berry Blitz Bonus Growth 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Bonus Growth 2", "Purchased Berry Blitz Bonus Growth 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Bonus Growth 3", "Purchased Berry Blitz Bonus Growth 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Blitz Bonus Growth 4", "Purchased Berry Blitz Bonus Growth 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Ability", "Purchased Berry Fountain Ability", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Cooldown 1", "Purchased Berry Fountain Cooldown 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Cooldown 2", "Purchased Berry Fountain Cooldown 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Cooldown 3", "Purchased Berry Fountain Cooldown 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Cooldown 4", "Purchased Berry Fountain Cooldown 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Fountain Cooldown 5", "Purchased Berry Fountain Cooldown 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Star Wand", "Purchased Star Wand", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase PopGun", "Purchased PopGun", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Berry Chooser", "Purchased Berry Chooser", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Trampoline", "Purchased Trampoline", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Star Orb Generator", "Purchased Star Orb Generator", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Auto Star Popper", "Purchased Auto Star Popper", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Bibble", "Purchased Bibble", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Star Key", "Purchased Star Key", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 1", "Purchased Rewind 1", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 2", "Purchased Rewind 2", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 3", "Purchased Rewind 3", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 4", "Purchased Rewind 4", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 5", "Purchased Rewind 5", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 6", "Purchased Rewind 6", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 7", "Purchased Rewind 7", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    upgrade_screen.add_event(
        "Purchase Rewind 8", "Purchased Rewind 8", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )        
        
        
    zone_1.add_event(
        "Bank 10 Coins", "Banked 10 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 25 Coins", "Banked 25 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 100 Coins", "Banked 100 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 250 Coins", "Banked 250 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 500 Coins", "Banked 500 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 1,000 Coins", "Banked 1,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 10 Stars", "Banked 10 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_1.add_event(
        "Bank 25 Stars", "Banked 25 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_1.add_event(
        "Consume 5 Gnomes", "Consumed 5 Gnomes", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_1.add_event(
        "Consume 5 Props", "Consumed 5 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_1.add_event(
        "Consume 25 Props", "Consumed 25 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
        
    zone_2.add_event(
        "Bank 2,500 Coins", "Banked 2,500 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 5,000 Coins", "Banked 5,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 10,000 Coins", "Banked 10,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 25,000 Coins", "Banked 25,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 50,000 Coins", "Banked 50,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 50 Stars", "Banked 50 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Bank 100 Stars", "Banked 100 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_2.add_event(
        "Consume 25 Gnomes", "Consumed 25 Gnomes", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_2.add_event(
        "Consume 50 Props", "Consumed 50 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
    zone_2.add_event(
        "Consume 75 Props", "Consumed 75 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
    zone_2.add_event(
        "Consume 100 Props", "Consumed 100 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
        
    zone_3.add_event(
        "Bank 100,000 Coins", "Banked 100,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_3.add_event(
        "Bank 250 Stars", "Banked 250 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_3.add_event(
        "Bank 500 Stars", "Banked 500 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_3.add_event(
        "Consume 50 Gnomes", "Consumed 50 Gnomes", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_3.add_event(
        "Consume 250 Props", "Consumed 250 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
        
    zone_4.add_event(
        "Bank 250,000 Coins", "Banked 250,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_4.add_event(
        "Bank 500,000 Coins", "Banked 500,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_4.add_event(
        "Bank 1,000 Stars", "Banked 1,000 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_4.add_event(
        "Bank 2,500 Stars", "Banked 2,500 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_4.add_event(
        "Consume 75 Gnomes", "Consumed 75 Gnomes", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_4.add_event(
        "Consume 500 Props", "Consumed 500 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
    zone_4.add_event(
        "Consume 750 Props", "Consumed 750 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
        
        
    zone_5.add_event(
        "Bank 1,000,000 Coins", "Banked 1,000,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Bank 2,000,000 Coins", "Banked 2,000,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Bank 10,000,000 Coins", "Banked 10,000,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Bank 25,000,000 Coins", "Banked 25,000,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
        
    zone_5.add_event(
        "Bank 50,000,000 Coins", "Banked 50,000,000 Coins", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Bank 5,000 Stars", "Banked 5,000 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Bank 9,999 Stars", "Banked 9,999 Stars", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )
        
    zone_5.add_event(
        "Consume 100 Gnomes", "Consumed 100 Gnomes", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )   
        
    zone_5.add_event(
        "Consume 1,000 Props", "Consumed 1,000 Props", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )  
    
    
    zone_5.add_event(
        "Open Star Door", "Victory", location_type=BerryBuryBerryLocation, item_type=items.BerryBuryBerryItem
        )

    # # If you create all your regions and locations line-by-line like this,
    # # the length of your create_regions might get out of hand.
    # # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # # However, it is worth understanding how the actual creation of regions and locations works,
    # # That way, we're not just mindlessly copy-pasting! :)
