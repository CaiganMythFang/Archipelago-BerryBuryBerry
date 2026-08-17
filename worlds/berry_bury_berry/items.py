from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BerryBuryBerryWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAME_TO_ID = {
    "Spawn Star": 1,
    "Progressive Berry Buddy": 2,
    "Progressive Sledgehammer": 3,
    "Movable Hole": 4,
    "Progressive Hole Range": 5,
    "Progressive Hole Speed": 6,
    "Vaccuum": 7,
    "Progressive Vaccuum Capacity": 8,
    "Auto Pickup Coins": 9,
    "Progressive Pickup Range": 10,
    "Chainsaw": 11,
    "Progressive JUICED Multiplier": 12,
    "Progressive Increase Day Length": 13,
    "Progressive Flower": 14,
    "Progressive Golden Berry Chance": 15,
    "Progressive Golden Berry Multiplier": 16,
    "Berry Blitz": 17,
    "Progressive Berry Blitz Duration": 18,
    "Progressive Berry Blitz Bonus Growth": 19,
    "Berry Fountain Ability": 20,
    "Progressive Berry Fountain Cooldown": 21,
    "Star Wand": 22,
    "PopGun": 23,
    "Berry Chooser": 24,
    "Trampoline": 25,
    "Star Orb Generator": 26,
    "Auto Star Popper": 27,
    "Bibble": 28,
    "Star Key": 29,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Spawn Star": ItemClassification.filler,
    "Progressive Berry Buddy": ItemClassification.useful,
    "Progressive Sledgehammer": ItemClassification.progression,
    "Movable Hole": ItemClassification.useful,
    "Progressive Hole Range": ItemClassification.useful,
    "Progressive Hole Speed": ItemClassification.useful,
    "Vaccuum": ItemClassification.progression,
    "Progressive Vaccuum Capacity": ItemClassification.useful,
    "Auto Pickup Coins": ItemClassification.useful,
    "Progressive Pickup Range": ItemClassification.useful,
    "Chainsaw": ItemClassification.useful,
    "Progressive JUICED Multiplier": ItemClassification.useful,
    "Progressive Increase Day Length": ItemClassification.useful,
    "Progressive Flower": ItemClassification.useful,
    "Progressive Golden Berry Chance": ItemClassification.useful,
    "Progressive Golden Berry Multiplier": ItemClassification.useful,
    "Berry Blitz": ItemClassification.useful,
    "Progressive Berry Blitz Duration": ItemClassification.useful,
    "Progressive Berry Blitz Bonus Growth": ItemClassification.useful,
    "Berry Fountain Ability": ItemClassification.useful,
    "Progressive Berry Fountain Cooldown": ItemClassification.useful,
    "Star Wand": ItemClassification.progression,
    "PopGun": ItemClassification.useful,
    "Berry Chooser": ItemClassification.useful,
    "Trampoline": ItemClassification.useful,
    "Star Orb Generator": ItemClassification.useful,
    "Auto Star Popper": ItemClassification.useful,
    "Bibble": ItemClassification.useful,
    "Star Key": ItemClassification.progression,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class BerryBuryBerryItem(Item):
    game = "BerryBuryBerry"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: BerryBuryBerryWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # # This ensures that generating with the same generator seed twice yields the same output.
    # # DO NOT use a bare random object from Python's built-in random module.
    # if world.random.randint(0, 99) < world.options.trap_chance:
        # return "Math Trap"
    return "Spawn Star"


def create_item_with_correct_classification(world: BerryBuryBerryWorld, name: str) -> BerryBuryBerryItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    # if name == "Health Upgrade" and world.options.hard_mode:
        # classification = ItemClassification.progression

    return BerryBuryBerryItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: BerryBuryBerryWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Berry Buddy"),
        world.create_item("Progressive Sledgehammer"),
        world.create_item("Progressive Sledgehammer"),
        world.create_item("Progressive Sledgehammer"),
        world.create_item("Progressive Sledgehammer"),
        world.create_item("Movable Hole"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Range"),
        world.create_item("Progressive Hole Speed"),
        world.create_item("Progressive Hole Speed"),
        world.create_item("Vaccuum"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Progressive Vaccuum Capacity"),
        world.create_item("Auto Pickup Coins"),
        world.create_item("Progressive Pickup Range"),
        world.create_item("Progressive Pickup Range"),
        world.create_item("Progressive Pickup Range"),
        world.create_item("Progressive Pickup Range"),
        world.create_item("Chainsaw"),
        world.create_item("Progressive JUICED Multiplier"),
        world.create_item("Progressive JUICED Multiplier"),
        world.create_item("Progressive JUICED Multiplier"),
        world.create_item("Progressive JUICED Multiplier"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Increase Day Length"),
        world.create_item("Progressive Flower"),
        world.create_item("Progressive Flower"),
        world.create_item("Progressive Golden Berry Chance"),
        world.create_item("Progressive Golden Berry Chance"),
        world.create_item("Progressive Golden Berry Chance"),
        world.create_item("Progressive Golden Berry Chance"),
        world.create_item("Progressive Golden Berry Multiplier"),
        world.create_item("Progressive Golden Berry Multiplier"),
        world.create_item("Progressive Golden Berry Multiplier"),
        world.create_item("Progressive Golden Berry Multiplier"),
        world.create_item("Progressive Golden Berry Multiplier"),
        world.create_item("Berry Blitz"),
        world.create_item("Progressive Berry Blitz Duration"),
        world.create_item("Progressive Berry Blitz Duration"),
        world.create_item("Progressive Berry Blitz Duration"),
        world.create_item("Progressive Berry Blitz Duration"),
        world.create_item("Progressive Berry Blitz Duration"),
        world.create_item("Progressive Berry Blitz Bonus Growth"),
        world.create_item("Progressive Berry Blitz Bonus Growth"),
        world.create_item("Progressive Berry Blitz Bonus Growth"),
        world.create_item("Progressive Berry Blitz Bonus Growth"),
        world.create_item("Berry Fountain Ability"),
        world.create_item("Progressive Berry Fountain Cooldown"),
        world.create_item("Progressive Berry Fountain Cooldown"),
        world.create_item("Progressive Berry Fountain Cooldown"),
        world.create_item("Progressive Berry Fountain Cooldown"),
        world.create_item("Progressive Berry Fountain Cooldown"),
        world.create_item("Star Wand"),
        world.create_item("PopGun"),
        world.create_item("Berry Chooser"),
        world.create_item("Trampoline"),
        world.create_item("Star Orb Generator"),
        world.create_item("Auto Star Popper"),
        world.create_item("Bibble"),
        world.create_item("Star Key"),
    ]

    # # Some items may only exist if the player enables certain options.
    # # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # # Otherwise, we add a filler Confetti Cannon.
    # if world.options.hammer:
        # # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # # it must be present in the worlds item_name_to_id.
        # # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        # itempool.append(world.create_item("Hammer"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # # Sometimes, you might want the player to start with certain items already in their inventory.
    # # These items are called "precollected items".
    # # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # # Players can add precollected items themselves via the generic "start_inventory" option.
    # # If you want to add your own precollected items, you can do so via world.push_precollected().
    # if world.options.start_with_one_confetti_cannon:
        # # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        # starting_confetti_cannon = world.create_item("Confetti Cannon")
        # world.push_precollected(starting_confetti_cannon)
