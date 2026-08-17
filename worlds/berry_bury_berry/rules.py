from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
# By default from the APQuest Rules.py, this section only has the first three. In /archipelago/rules_builder/rules.py, you can find many more helper methods, including the last 3 here.
from rule_builder.rules import Has, HasAll, Rule, CanReachLocation, CanReachRegion, HasFromList

from .options import PropSanity

if TYPE_CHECKING:
    from .world import BerryBuryBerryWorld

# Define how many Progressive Sledgehammers we need to move to the next Region

SLEDGEHAMMER_1_KEY = Has("Progressive Sledgehammer", count=1)
SLEDGEHAMMER_2_KEY = Has("Progressive Sledgehammer", count=2)
SLEDGEHAMMER_3_KEY = Has("Progressive Sledgehammer", count=3)
SLEDGEHAMMER_4_KEY = Has("Progressive Sledgehammer", count=4)


def set_all_rules(world: BerryBuryBerryWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: BerryBuryBerryWorld) -> None:
    # Define the entrances between zones
    upgrade_to_zone_1 = world.get_entrance("Upgrade Screen to Zone 1")
    zone_1_to_zone_2 = world.get_entrance("Zone 1 to Zone 2")
    zone_2_to_zone_3 = world.get_entrance("Zone 2 to Zone 3")
    zone_3_to_zone_4 = world.get_entrance("Zone 3 to Zone 4")
    zone_4_to_zone_5 = world.get_entrance("Zone 4 to Zone 5")

    # # Now, let's make some rules!
    # # First, let's handle the transition from the overworld to the bottom right room,
    # # which requires slashing a bush with the Sword.
    # # For this, we need a rule that says "player has a Sword".
    # # We can use a "Has"-type rule from the rule_builder module for this.
    # break_level_1_walls = Has("Sword")

    # # Now we can set our "can_destroy_bush" rule to the entrance which requires slashing a bush to clear the path.
    # # The easiest way to do this is by calling world.set_rule, which works for both Locations and Entrances.
    # world.set_rule(overworld_to_bottom_right_room, can_destroy_bush)

    # # Conditions can also depend on event items.
    # button_pressed = Has("Top Left Room Button Pressed")
    # world.set_rule(right_room_to_final_boss_room, button_pressed)

    # # Some entrance rules may only apply if the player enabled certain options.
    # # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # # Overworld to the Top Middle Room.
    # if world.options.hammer:
        # overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
        # can_smash_brick = Has("Hammer")
        # world.set_rule(overworld_to_top_middle_room, can_smash_brick)

    # # So far, we've been using "Has" from the Rule Builder to make our rules.
    # # There is another way to make rules that you will see in a lot of older worlds.
    # # A rule can just be a function that takes a "state" argument and returns a bool.
    # # As a demonstration of what that looks like, let's do it with our final Entrance rule:
    # world.set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))
    # # This style is not really recommended anymore, though.
    # # Notice how you have to explicitly capture world.player here so that the rule applies to the correct player?
    # # Well, Rule Builder does this part for you, inside of world.set_rule.
    # # This doesn't just result in shorter code, it also means you can define rules statically (at the module level).
    # # APQuest opts to create its Rule objects locally, but just to show what this would look like,
    # # we'll re-set the "Overworld to Top Left Room" rule to a constant defined at the top of this file:
    # world.set_rule(overworld_to_top_left_room, HAS_KEY)
    
    # Define the Sledgehammer count needed for each Region Entrance
    world.set_rule(zone_1_to_zone_2, SLEDGEHAMMER_1_KEY)
    world.set_rule(zone_2_to_zone_3, SLEDGEHAMMER_2_KEY)
    world.set_rule(zone_3_to_zone_4, SLEDGEHAMMER_3_KEY)
    world.set_rule(zone_4_to_zone_5, SLEDGEHAMMER_4_KEY)

    # Beyond these structural advantages,
    # Rule Builder also allows the core AP code to do a lot of under-the-hood optimizations.
    # Rule Builder is quite comprehensive, and even if you have really esoteric rules,
    # you can make custom rules by subclassing CustomRule.

def set_all_location_rules(world: BerryBuryBerryWorld) -> None:
    # # Location rules work no differently from Entrance rules.
    # # Most of our locations are chests that can simply be opened by walking up to them.
    # # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # # reach the region that the chest sits in.
    # # However, our two enemies work differently.
    # # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # # So, we need to set requirements on the Locations themselves.
    # # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.

    # # In "set_all_entrance_rules", we had a rule for a location that doesn't always exist.
    # # In this case, we had to check for its existence (by checking the player's chosen options) before setting the rule.
    # # Other times, you may have a situation where a location can have two different rules depending on the options.
    # # In our case, the enemy in the right room has more health if hard mode is selected,
    # # so ontop of the Sword, the player will either need one more health or a Shield in hard mode.
    # # First, let's make our sword condition.
    # can_defeat_basic_enemy: Rule = Has("Progressive Sledgehammer")

    # # Next, we'll check whether hard mode has been chosen in the player options.
    # if world.options.hard_mode:
        # # We'll make the condition for "Has a Shield or a Health Upgrade".
        # # We can chain two "Has" conditions together with the | operator to make "Has Shield or has Health Upgrade".
        # can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")

        # # Now, we chain this rule to our Sword rule.
        # # Since we want both conditions to be true, in this case, we have to chain them in an "and" way.
        # # For this, we can use the & operator.
        # can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit

    # # Finally, we set our rule onto the Right Room Eney Drop location.
    # right_room_enemy = world.get_location("Right Room Enemy Drop")
    # world.set_rule(right_room_enemy, can_defeat_basic_enemy)
    
    # The Upgrade Screen has most purchases require the previous tier, so we need to set the rule for each shop purchase to require all previous tier purchases.
    # We set location/item pairing events in the events section of location.py. When someone purchases an upgrade, it will give them the matching item, which we will look for higher tier upgrades.
    
    # Define which Location check this rule is for.
    purchase_berry_buddy_2 = world.get_location("Shop Berry Buddy 2")
    # Define the requirement for this rule: for us, its what previous upgrade tiers are needed for this tier. Using HasFromList, we start by listing every item, then end with a count=# that matches how many of these are needed. For our needs, the player needs EVERY previous tier of this upgrade, as well as having banked the closest amount of coins.
    purchased_berry_buddy_1 = HasFromList("Purchased Berry Buddy 1", "Banked 10 Coins", count=2)
    # Finally, we define the rule itself with world.set_rule(), starting with the location this rule is for, and then the requirements it needs. In this case, we're saying that to be able to purchase Berry Buddy 2, the player needs to purchase Berry Buddy 1 first, and have banked 10 Coins, the cost of this upgrade slot
    world.set_rule(purchase_berry_buddy_2, purchased_berry_buddy_1)
    # Since Berry Buddy 1 is not locked behind a lower tier and is available from the start, it does not need to be defined in the rules.
    
    purchase_berry_buddy_3 = world.get_location("Shop Berry Buddy 3")
    purchased_berry_buddy_2 = HasFromList("Purchased Berry Buddy 1", "Purchased Berry Buddy 2", "Banked 100 Coins", count=3)
    world.set_rule(purchase_berry_buddy_3, purchased_berry_buddy_2)
    
    purchase_berry_buddy_4 = world.get_location("Shop Berry Buddy 4")
    purchased_berry_buddy_3 = HasFromList("Purchased Berry Buddy 1", "Purchased Berry Buddy 2", "Purchased Berry Buddy 3", "Banked 1,000 Coins", count=4)
    world.set_rule(purchase_berry_buddy_4, purchased_berry_buddy_3)
    
    purchase_berry_buddy_5 = world.get_location("Shop Berry Buddy 5")
    purchased_berry_buddy_4 = HasFromList("Purchased Berry Buddy 1", "Purchased Berry Buddy 2", "Purchased Berry Buddy 3", "Purchased Berry Buddy 4", "Banked 10,000 Coins", count=5)
    world.set_rule(purchase_berry_buddy_5, purchased_berry_buddy_4)
    
    purchase_berry_buddy_6 = world.get_location("Shop Berry Buddy 6")
    purchased_berry_buddy_5 = HasFromList("Purchased Berry Buddy 1", "Purchased Berry Buddy 2", "Purchased Berry Buddy 3", "Purchased Berry Buddy 4", "Purchased Berry Buddy 5", "Banked 100,000 Coins", count=6)
    world.set_rule(purchase_berry_buddy_6, purchased_berry_buddy_5)
    
    purchase_berry_buddy_7 = world.get_location("Shop Berry Buddy 7")
    purchased_berry_buddy_6 = HasFromList("Purchased Berry Buddy 1", "Purchased Berry Buddy 2", "Purchased Berry Buddy 3", "Purchased Berry Buddy 4", "Purchased Berry Buddy 5", "Purchased Berry Buddy 6", "Banked 1,000,000 Coins", count=7)
    world.set_rule(purchase_berry_buddy_7, purchased_berry_buddy_6)
    
    
    purchase_sledgehammer_2 = world.get_location("Shop Sledgehammer 2")
    purchased_sledgehammer_1 = HasFromList("Purchased Sledgehammer 1", "Banked 10,000 Coins", count=2)
    world.set_rule(purchase_sledgehammer_2, purchased_sledgehammer_1)
    
    purchase_sledgehammer_3 = world.get_location("Shop Sledgehammer 3")
    purchased_sledgehammer_2 = HasFromList("Purchased Sledgehammer 2", "Purchased Sledgehammer 1", "Banked 100,000 Coins", count=3)
    world.set_rule(purchase_sledgehammer_3, purchased_sledgehammer_2)
    
    purchase_sledgehammer_4 = world.get_location("Shop Sledgehammer 4")
    purchased_sledgehammer_3 = HasFromList("Purchased Sledgehammer 3", "Purchased Sledgehammer 2", "Purchased Sledgehammer 1", "Banked 1,000,000 Coins", count=4)
    world.set_rule(purchase_sledgehammer_4, purchased_sledgehammer_3)
    
    
    purchase_hole_range_1 = world.get_location("Shop Hole Range 1")
    purchased_movable_hole = HasFromList("Purchased Movable Hole", "Banked 100 Coins", count=2)
    world.set_rule(purchase_hole_range_1, purchased_movable_hole)
    
    purchase_hole_range_2 = world.get_location("Shop Hole Range 2")
    purchased_hole_range_1 = HasFromList("Purchased Hole Range 1", "Purchased Movable Hole", "Banked 500 Coins", count=3)
    world.set_rule(purchase_hole_range_2, purchased_hole_range_1)
    
    purchase_hole_range_3 = world.get_location("Shop Hole Range 3")
    purchased_hole_range_2 = HasFromList("Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 10,000 Coins", count=4)
    world.set_rule(purchase_hole_range_3, purchased_hole_range_2)
    
    purchase_hole_range_4 = world.get_location("Shop Hole Range 4")
    purchased_hole_range_3 = HasFromList("Purchased Hole Range 3", "Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 25,000 Coins", count=5)
    world.set_rule(purchase_hole_range_4, purchased_hole_range_3)
    
    purchase_hole_range_5 = world.get_location("Shop Hole Range 5")
    purchased_hole_range_4 = HasFromList("Purchased Hole Range 4", "Purchased Hole Range 3", "Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 250,000 Coins", count=6)
    world.set_rule(purchase_hole_range_5, purchased_hole_range_4)
    
    purchase_hole_range_6 = world.get_location("Shop Hole Range 6")
    purchased_hole_range_5 = HasFromList("Purchased Hole Range 5", "Purchased Hole Range 4", "Purchased Hole Range 3", "Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 500,000 Coins", count=7)
    world.set_rule(purchase_hole_range_6, purchased_hole_range_5)
    
    purchase_hole_range_7 = world.get_location("Shop Hole Range 7")
    purchased_hole_range_6 = HasFromList("Purchased Hole Range 6", "Purchased Hole Range 5", "Purchased Hole Range 4", "Purchased Hole Range 3", "Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 1,000,000 Coins", count=8)
    world.set_rule(purchase_hole_range_7, purchased_hole_range_6)
    
    purchase_hole_range_8 = world.get_location("Shop Hole Range 8")
    purchased_hole_range_7 = HasFromList("Purchased Hole Range 7", "Purchased Hole Range 6", "Purchased Hole Range 5", "Purchased Hole Range 4", "Purchased Hole Range 3", "Purchased Hole Range 2", "Purchased Hole Range 1", "Purchased Movable Hole", "Banked 1,000,000 Coins", count=9)
    world.set_rule(purchase_hole_range_8, purchased_hole_range_7)
    
    
    purchase_hole_speed_1 = world.get_location("Shop Hole Speed 1")
    purchased_movable_hole = HasFromList("Purchased Movable Hole", "Banked 10,000 Coins", count=2)
    world.set_rule(purchase_hole_speed_1, purchased_movable_hole)
    
    purchase_hole_speed_2 = world.get_location("Shop Hole Speed 2")
    purchased_hole_speed_1 = HasFromList("Purchased Hole Speed 1", "Purchased Movable Hole", "Banked 500,000 Coins", count=3)
    world.set_rule(purchase_hole_speed_2, purchased_hole_speed_1)
    
    
    purchase_vaccuum_capacity_1 = world.get_location("Shop Vaccuum Capacity 1")
    purchased_vaccuum = HasFromList("Purchased Vaccuum", "Banked 1,000 Coins", count=2)
    world.set_rule(purchase_vaccuum_capacity_1, purchased_vaccuum)
    
    purchase_vaccuum_capacity_2 = world.get_location("Shop Vaccuum Capacity 2")
    purchased_vaccuum_capacity_1 = HasFromList("Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 10,000 Coins", count=3)
    world.set_rule(purchase_vaccuum_capacity_2, purchased_vaccuum_capacity_1)
    
    purchase_vaccuum_capacity_3 = world.get_location("Shop Vaccuum Capacity 3")
    purchased_vaccuum_capacity_2 = HasFromList("Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 50,000 Coins", count=4)
    world.set_rule(purchase_vaccuum_capacity_3, purchased_vaccuum_capacity_2)
    
    purchase_vaccuum_capacity_4 = world.get_location("Shop Vaccuum Capacity 4")
    purchased_vaccuum_capacity_3 = HasFromList("Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 100,000 Coins", count=5)
    world.set_rule(purchase_vaccuum_capacity_4, purchased_vaccuum_capacity_3)
    
    purchase_vaccuum_capacity_5 = world.get_location("Shop Vaccuum Capacity 5")
    purchased_vaccuum_capacity_4 = HasFromList("Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 250,000 Coins", count=6)
    world.set_rule(purchase_vaccuum_capacity_5, purchased_vaccuum_capacity_4)
    
    purchase_vaccuum_capacity_6 = world.get_location("Shop Vaccuum Capacity 6")
    purchased_vaccuum_capacity_5 = HasFromList("Purchased Vaccuum Capacity 5", "Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 500,000 Coins", count=7)
    world.set_rule(purchase_vaccuum_capacity_6, purchased_vaccuum_capacity_5)
    
    purchase_vaccuum_capacity_7 = world.get_location("Shop Vaccuum Capacity 7")
    purchased_vaccuum_capacity_6 = HasFromList("Purchased Vaccuum Capacity 6", "Purchased Vaccuum Capacity 5", "Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 1,000,000 Coins", count=8)
    world.set_rule(purchase_vaccuum_capacity_7, purchased_vaccuum_capacity_6)
    
    purchase_vaccuum_capacity_8 = world.get_location("Shop Vaccuum Capacity 8")
    purchased_vaccuum_capacity_7 = HasFromList("Purchased Vaccuum Capacity 7", "Purchased Vaccuum Capacity 6", "Purchased Vaccuum Capacity 5", "Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 2,000,000 Coins", count=9)
    world.set_rule(purchase_vaccuum_capacity_8, purchased_vaccuum_capacity_7)
    
    purchase_vaccuum_capacity_9 = world.get_location("Shop Vaccuum Capacity 9")
    purchased_vaccuum_capacity_8 = HasFromList("Purchased Vaccuum Capacity 8", "Purchased Vaccuum Capacity 7", "Purchased Vaccuum Capacity 6", "Purchased Vaccuum Capacity 5", "Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 2,000,000 Coins", count=10)
    world.set_rule(purchase_vaccuum_capacity_9, purchased_vaccuum_capacity_8)
    
    purchase_vaccuum_capacity_10 = world.get_location("Shop Vaccuum Capacity 10")
    purchased_vaccuum_capacity_9 = HasFromList("Purchased Vaccuum Capacity 9", "Purchased Vaccuum Capacity 8", "Purchased Vaccuum Capacity 7", "Purchased Vaccuum Capacity 6", "Purchased Vaccuum Capacity 5", "Purchased Vaccuum Capacity 4", "Purchased Vaccuum Capacity 3", "Purchased Vaccuum Capacity 2", "Purchased Vaccuum Capacity 1", "Purchased Vaccuum", "Banked 2,000,000 Coins", count=11)
    world.set_rule(purchase_vaccuum_capacity_10, purchased_vaccuum_capacity_9)
    
    
    purchase_auto_pickup_range_1 = world.get_location("Shop Auto Pickup Range 1")
    purchased_auto_pickup_coins = HasFromList("Purchased Auto Pickup Coins", "Banked 2,500 Coins", count=2)
    world.set_rule(purchase_auto_pickup_range_1, purchased_auto_pickup_coins)
        
    purchase_auto_pickup_range_2 = world.get_location("Shop Auto Pickup Range 2")
    purchased_auto_pickup_range_1 = HasFromList("Purchased Auto Pickup Range 1", "Purchased Auto Pickup Coins", "Banked 25,000 Coins", count=3)
    world.set_rule(purchase_auto_pickup_range_2, purchased_auto_pickup_range_1)
        
    purchase_auto_pickup_range_3 = world.get_location("Shop Auto Pickup Range 3")
    purchased_auto_pickup_range_2 = HasFromList("Purchased Auto Pickup Range 2", "Purchased Auto Pickup Range 1", "Purchased Auto Pickup Coins", "Banked 100,000 Coins", count=4)
    world.set_rule(purchase_auto_pickup_range_3, purchased_auto_pickup_range_2)
        
    purchase_auto_pickup_range_4 = world.get_location("Shop Auto Pickup Range 4")
    purchased_auto_pickup_range_3 = HasFromList("Purchased Auto Pickup Range 3", "Purchased Auto Pickup Range 2", "Purchased Auto Pickup Range 1", "Purchased Auto Pickup Coins", "Banked 1,000,000 Coins", count=5)
    world.set_rule(purchase_auto_pickup_range_4, purchased_auto_pickup_range_3)
    
    
    purchase_juiced_multiplier_1 = world.get_location("Shop JUICED Multiplier 1")
    purchased_chainsaw = HasFromList("Purchased Chainsaw", "Banked 250,000 Coins", count=2)
    world.set_rule(purchase_juiced_multiplier_1, purchased_chainsaw)
    
    purchase_juiced_multiplier_2 = world.get_location("Shop JUICED Multiplier 2")
    purchased_juiced_multiplier_1 = HasFromList("Purchased JUICED Multiplier 1", "Purchased Chainsaw", "Banked 1,000,000 Coins", count=3)
    world.set_rule(purchase_juiced_multiplier_2, purchased_juiced_multiplier_1)
    
    purchase_juiced_multiplier_3 = world.get_location("Shop JUICED Multiplier 3")
    purchased_juiced_multiplier_2 = HasFromList("Purchased JUICED Multiplier 2", "Purchased JUICED Multiplier 1", "Purchased Chainsaw", "Banked 10,000,000 Coins", count=4)
    world.set_rule(purchase_juiced_multiplier_3, purchased_juiced_multiplier_2)
    
    purchase_juiced_multiplier_4 = world.get_location("Shop JUICED Multiplier 4")
    purchased_juiced_multiplier_3 = HasFromList("Purchased JUICED Multiplier 3", "Purchased JUICED Multiplier 2", "Purchased JUICED Multiplier 1", "Purchased Chainsaw", "Banked 50,000,000 Coins", count=5)
    world.set_rule(purchase_juiced_multiplier_4, purchased_juiced_multiplier_3)
    
    
    purchase_increase_day_length_2 = world.get_location("Shop Increase Day Length 2")
    purchased_increase_day_length_1 = HasFromList("Purchased Increase Day Length 1", "Banked 1,000 Coins", count=2)
    world.set_rule(purchase_increase_day_length_2, purchased_increase_day_length_1)
    
    purchase_increase_day_length_3 = world.get_location("Shop Increase Day Length 3")
    purchased_increase_day_length_2 = HasFromList("Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 2,500 Coins", count=3)
    world.set_rule(purchase_increase_day_length_3, purchased_increase_day_length_2)
    
    purchase_increase_day_length_4 = world.get_location("Shop Increase Day Length 4")
    purchased_increase_day_length_3 = HasFromList("Purchased Increase Day Length 3", "Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 10,000 Coins", count=4)
    world.set_rule(purchase_increase_day_length_4, purchased_increase_day_length_3)
    
    purchase_increase_day_length_5 = world.get_location("Shop Increase Day Length 5")
    purchased_increase_day_length_4 = HasFromList("Purchased Increase Day Length 4", "Purchased Increase Day Length 3", "Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 50,000 Coins", count=5)
    world.set_rule(purchase_increase_day_length_5, purchased_increase_day_length_4)
    
    purchase_increase_day_length_6 = world.get_location("Shop Increase Day Length 6")
    purchased_increase_day_length_5 = HasFromList("Purchased Increase Day Length 5", "Purchased Increase Day Length 4", "Purchased Increase Day Length 3", "Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 250,000 Coins", count=6)
    world.set_rule(purchase_increase_day_length_6, purchased_increase_day_length_5)
    
    purchase_increase_day_length_7 = world.get_location("Shop Increase Day Length 7")
    purchased_increase_day_length_6 = HasFromList("Purchased Increase Day Length 6", "Purchased Increase Day Length 5", "Purchased Increase Day Length 4", "Purchased Increase Day Length 3", "Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 1,000,000 Coins", count=7)
    world.set_rule(purchase_increase_day_length_7, purchased_increase_day_length_6)
    
    purchase_increase_day_length_8 = world.get_location("Shop Increase Day Length 8")
    purchased_increase_day_length_7 = HasFromList("Purchased Increase Day Length 7", "Purchased Increase Day Length 6", "Purchased Increase Day Length 5", "Purchased Increase Day Length 4", "Purchased Increase Day Length 3", "Purchased Increase Day Length 2", "Purchased Increase Day Length 1", "Banked 50,000,000 Coins", count=8)
    world.set_rule(purchase_increase_day_length_8, purchased_increase_day_length_7)
    
    
    purchase_bush_to_tree = world.get_location("Shop Bush to Tree")
    purchased_flower_to_bush = HasFromList("Purchased Flower to Bush", "Banked 1,000,000 Coins", count=2)
    world.set_rule(purchase_bush_to_tree, purchased_flower_to_bush)
    
    
    purchase_golden_berry_chance_2 = world.get_location("Shop Golden Berry Chance 2")
    purchased_golden_berry_chance_1 = HasFromList("Purchased Golden Berry Chance 1", "Banked 250,000 Coins", count=2)
    world.set_rule(purchase_golden_berry_chance_2, purchased_golden_berry_chance_1)
    
    purchase_golden_berry_chance_3 = world.get_location("Shop Golden Berry Chance 3")
    purchased_golden_berry_chance_2 = HasFromList("Purchased Golden Berry Chance 2", "Purchased Golden Berry Chance 1", "Banked 2,000,000 Coins", count=3)
    world.set_rule(purchase_golden_berry_chance_3, purchased_golden_berry_chance_2)
    
    purchase_golden_berry_chance_4 = world.get_location("Shop Golden Berry Chance 4")
    purchased_golden_berry_chance_3 = HasFromList("Purchased Golden Berry Chance 3", "Purchased Golden Berry Chance 2", "Purchased Golden Berry Chance 1", "Banked 50,000,000 Coins", count=4)
    world.set_rule(purchase_golden_berry_chance_4, purchased_golden_berry_chance_3)
    
    
    purchase_golden_berry_multiplier_2 = world.get_location("Shop Golden Berry Multiplier 2")
    purchased_golden_berry_multiplier_1 = HasFromList("Purchased Golden Berry Multiplier 1", "Banked 100,000 Coins", count=2)
    world.set_rule(purchase_golden_berry_multiplier_2, purchased_golden_berry_multiplier_1)
    
    purchase_golden_berry_multiplier_3 = world.get_location("Shop Golden Berry Multiplier 3")
    purchased_golden_berry_multiplier_2 = HasFromList("Purchased Golden Berry Multiplier 2", "Purchased Golden Berry Multiplier 1", "Banked 500,000 Coins", count=3)
    world.set_rule(purchase_golden_berry_multiplier_3, purchased_golden_berry_multiplier_2)
    
    purchase_golden_berry_multiplier_4 = world.get_location("Shop Golden Berry Multiplier 4")
    purchased_golden_berry_multiplier_3 = HasFromList("Purchased Golden Berry Multiplier 3", "Purchased Golden Berry Multiplier 2", "Purchased Golden Berry Multiplier 1", "Banked 1,000,000 Coins", count=4)
    world.set_rule(purchase_golden_berry_multiplier_4, purchased_golden_berry_multiplier_3)
    
    purchase_golden_berry_multiplier_5 = world.get_location("Shop Golden Berry Multiplier 5")
    purchased_golden_berry_multiplier_4 = HasFromList("Purchased Golden Berry Multiplier 4", "Purchased Golden Berry Multiplier 3", "Purchased Golden Berry Multiplier 2", "Purchased Golden Berry Multiplier 1", "Banked 50,000,000 Coins", count=5)
    world.set_rule(purchase_golden_berry_multiplier_5, purchased_golden_berry_multiplier_4)
    
    
    purchase_berry_blitz_duration_1 = world.get_location("Shop Berry Blitz Duration 1")
    purchased_berry_blitz = HasFromList("Purchased Berry Blitz", "Banked 1,000 Coins", count=2)
    world.set_rule(purchase_berry_blitz_duration_1, purchased_berry_blitz)
    
    purchase_berry_blitz_duration_2 = world.get_location("Shop Berry Blitz Duration 2")
    purchased_berry_blitz_duration_1 = HasFromList("Purchased Berry Blitz Duration 1", "Purchased Berry Blitz", "Banked 10,000 Coins", count=3)
    world.set_rule(purchase_berry_blitz_duration_2, purchased_berry_blitz_duration_1)
    
    purchase_berry_blitz_duration_3 = world.get_location("Shop Berry Blitz Duration 3")
    purchased_berry_blitz_duration_2 = HasFromList("Purchased Berry Blitz Duration 2", "Purchased Berry Blitz Duration 1", "Purchased Berry Blitz", "Banked 250,000 Coins", count=4)
    world.set_rule(purchase_berry_blitz_duration_3, purchased_berry_blitz_duration_2)
    
    purchase_berry_blitz_duration_4 = world.get_location("Shop Berry Blitz Duration 4")
    purchased_berry_blitz_duration_3 = HasFromList("Purchased Berry Blitz Duration 3", "Purchased Berry Blitz Duration 2", "Purchased Berry Blitz Duration 1", "Purchased Berry Blitz", "Banked 1,000,000 Coins", count=5)
    world.set_rule(purchase_berry_blitz_duration_4, purchased_berry_blitz_duration_3)
    
    purchase_berry_blitz_duration_5 = world.get_location("Shop Berry Blitz Duration 5")
    purchased_berry_blitz_duration_4 = HasFromList("Purchased Berry Blitz Duration 4", "Purchased Berry Blitz Duration 3", "Purchased Berry Blitz Duration 2", "Purchased Berry Blitz Duration 1", "Purchased Berry Blitz", "Banked 25,000,000 Coins", count=6)
    world.set_rule(purchase_berry_blitz_duration_5, purchased_berry_blitz_duration_4)
    
    
    purchase_berry_blitz_bonus_growth_1 = world.get_location("Shop Berry Blitz Bonus Growth 1")
    purchased_berry_blitz = HasFromList("Purchased Berry Blitz", "Banked 2,500 Coins", count=2)
    world.set_rule(purchase_berry_blitz_bonus_growth_1, purchased_berry_blitz)
    
    purchase_berry_blitz_bonus_growth_2 = world.get_location("Shop Berry Blitz Bonus Growth 2")
    purchased_berry_blitz_bonus_growth_1 = HasFromList("Purchased Berry Blitz Bonus Growth 1","Purchased Berry Blitz", "Banked 100,000 Coins", count=3)
    world.set_rule(purchase_berry_blitz_bonus_growth_2, purchased_berry_blitz_bonus_growth_1)
    
    purchase_berry_blitz_bonus_growth_3 = world.get_location("Shop Berry Blitz Bonus Growth 3")
    purchased_berry_blitz_bonus_growth_2 = HasFromList("Purchased Berry Blitz Bonus Growth 2", "Purchased Berry Blitz Bonus Growth 1","Purchased Berry Blitz", "Banked 1,000,000 Coins", count=4)
    world.set_rule(purchase_berry_blitz_bonus_growth_3, purchased_berry_blitz_bonus_growth_2)
    
    purchase_berry_blitz_bonus_growth_4 = world.get_location("Shop Berry Blitz Bonus Growth 4")
    purchased_berry_blitz_bonus_growth_3 = HasFromList("Purchased Berry Blitz Bonus Growth 3", "Purchased Berry Blitz Bonus Growth 2", "Purchased Berry Blitz Bonus Growth 1","Purchased Berry Blitz", "Banked 50,000,000 Coins", count=5)
    world.set_rule(purchase_berry_blitz_bonus_growth_4, purchased_berry_blitz_bonus_growth_3)
    
    
    purchase_berry_fountain_cooldown_1 = world.get_location("Shop Berry Fountain Cooldown 1")
    purchased_berry_fountain_ability = HasFromList("Purchased Berry Fountain Ability", "Banked 25,000 Coins", count=2)
    world.set_rule(purchase_berry_fountain_cooldown_1, purchased_berry_fountain_ability)
    
    purchase_berry_fountain_cooldown_2 = world.get_location("Shop Berry Fountain Cooldown 2")
    purchased_berry_fountain_cooldown_1 = HasFromList("Purchased Berry Fountain Cooldown 1", "Purchased Berry Fountain Ability", "Banked 100,000 Coins", count=3)
    world.set_rule(purchase_berry_fountain_cooldown_2, purchased_berry_fountain_cooldown_1)
    
    purchase_berry_fountain_cooldown_3 = world.get_location("Shop Berry Fountain Cooldown 3")
    purchased_berry_fountain_cooldown_2 = HasFromList("Purchased Berry Fountain Cooldown 2", "Purchased Berry Fountain Cooldown 1", "Purchased Berry Fountain Ability", "Banked 500,000 Coins", count=4)
    world.set_rule(purchase_berry_fountain_cooldown_3, purchased_berry_fountain_cooldown_2)
    
    purchase_berry_fountain_cooldown_4 = world.get_location("Shop Berry Fountain Cooldown 4")
    purchased_berry_fountain_cooldown_3 = HasFromList("Purchased Berry Fountain Cooldown 3", "Purchased Berry Fountain Cooldown 2", "Purchased Berry Fountain Cooldown 1", "Purchased Berry Fountain Ability", "Banked 2,000,000 Coins", count=5)
    world.set_rule(purchase_berry_fountain_cooldown_4, purchased_berry_fountain_cooldown_3)
    
    purchase_berry_fountain_cooldown_5 = world.get_location("Shop Berry Fountain Cooldown 5")
    purchased_berry_fountain_cooldown_4 = HasFromList("Purchased Berry Fountain Cooldown 4", "Purchased Berry Fountain Cooldown 3", "Purchased Berry Fountain Cooldown 2", "Purchased Berry Fountain Cooldown 1", "Purchased Berry Fountain Ability", "Banked 50,000,000 Coins", count=6)
    world.set_rule(purchase_berry_fountain_cooldown_5, purchased_berry_fountain_cooldown_4)
    
    
    purchase_star_wand = world.get_location("Shop Star Wand")
    purchased_star_wand = HasFromList("Banked 10 Coins", "Banked 25 Coins", count=2)
    world.set_rule(purchase_star_wand, purchased_star_wand)
    
    
    purchase_pop_gun = world.get_location("Shop PopGun")
    purchased_pop_gun = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", count=8)
    world.set_rule(purchase_pop_gun, purchased_pop_gun)
    
    
    purchase_berry_chooser = world.get_location("Shop Berry Chooser")
    purchased_berry_chooser = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", count=13)
    world.set_rule(purchase_berry_chooser, purchased_berry_chooser)
    
    
    purchase_trampoline = world.get_location("Shop Trampoline")
    purchased_trampoline = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", count=13)
    world.set_rule(purchase_trampoline, purchased_trampoline)
    
    
    purchase_star_orb_popper = world.get_location("Shop Auto Star Orb Popper")
    purchased_star_orb_popper = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", count=11)
    world.set_rule(purchase_star_orb_popper, purchased_star_orb_popper)
    
    
    purchase_bibble = world.get_location("Shop Bibble")
    purchased_bibble = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", count=9)
    world.set_rule(purchase_bibble, purchased_bibble)
    
    
    purchase_star_key = world.get_location("Shop Berry Chooser")
    purchased_star_key = HasFromList("Banked 10 Coins", "Banked 25 Coins", "Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", "Banked 1,000,000 Coins", "Banked 2,000,000 Coins", count=16)
    world.set_rule(purchase_star_key, purchased_star_key)
    
    
    consume_gnomes_2 = world.get_location("Consume 25 Gnomes")
    consumed_gnomes_1 = HasFromList("Consumed 5 Gnomes", count=1)
    world.set_rule(consume_gnomes_2, consumed_gnomes_1)
    
    consume_gnomes_3 = world.get_location("Consume 50 Gnomes")
    consumed_gnomes_2 = HasFromList("Consumed 25 Gnomes", "Consumed 5 Gnomes", count=2)
    world.set_rule(consume_gnomes_3, consumed_gnomes_2)
    
    consume_gnomes_4 = world.get_location("Consume 75 Gnomes")
    consumed_gnomes_3 = HasFromList("Consumed 50 Gnomes", "Consumed 25 Gnomes", "Consumed 5 Gnomes", count=3)
    world.set_rule(consume_gnomes_4, consumed_gnomes_3)
    
    consume_gnomes_5 = world.get_location("Consume 100 Gnomes")
    consumed_gnomes_4 = HasFromList("Consumed 75 Gnomes", "Consumed 50 Gnomes", "Consumed 25 Gnomes", "Consumed 5 Gnomes", count=4)
    world.set_rule(consume_gnomes_5, consumed_gnomes_4)
    
    
    consume_props_9 = world.get_location("Consume 1,000 Props")
    consumed_props_8 = HasFromList("Consumed 750 Props", "Consumed 500 Props", "Consumed 250 Props", "Consumed 100 Props", "Consumed 75 Props", "Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=8)
    world.set_rule(consume_props_9, consumed_props_8)
    
    consume_props_8= world.get_location("Consume 750 Props")
    consumed_props_7 = HasFromList("Consumed 500 Props", "Consumed 250 Props", "Consumed 100 Props", "Consumed 75 Props", "Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=7)
    world.set_rule(consume_props_8, consumed_props_7)
    
    consume_props_7= world.get_location("Consume 500 Props")
    consumed_props_6 = HasFromList("Consumed 250 Props", "Consumed 100 Props", "Consumed 75 Props", "Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=6)
    world.set_rule(consume_props_7, consumed_props_6)
    
    consume_props_6= world.get_location("Consume 250 Props")
    consumed_props_5 = HasFromList("Consumed 100 Props", "Consumed 75 Props", "Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=5)
    world.set_rule(consume_props_6, consumed_props_5)
    
    consume_props_5= world.get_location("Consume 100 Props")
    consumed_props_4 = HasFromList("Consumed 75 Props", "Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=4)
    world.set_rule(consume_props_5, consumed_props_4)
    
    consume_props_4= world.get_location("Consume 75 Props")
    consumed_props_3 = HasFromList("Consumed 50 Props", "Consumed 25 Props", "Consumed 5 Props", count=3)
    world.set_rule(consume_props_4, consumed_props_3)
    
    consume_props_3= world.get_location("Consume 50 Props")
    consumed_props_2 = HasFromList("Consumed 25 Props", "Consumed 5 Props", count=2)
    world.set_rule(consume_props_3, consumed_props_2)
    
    consume_props_2= world.get_location("Consume 25 Props")
    consumed_props_1 = HasFromList("Consumed 5 Props", count=1)
    world.set_rule(consume_props_2, consumed_props_1)
    
    
    bank_coins_19 = world.get_location("Bank 50,000,000 Coins")
    banked_coins_18 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", "Banked 1,000,000 Coins", "Banked 2,000,000 Coins", "Banked 10,000,000 Coins", "Banked 25,000,000 Coins", count=16)
    world.set_rule(bank_coins_19, banked_coins_18)
    
    bank_coins_18 = world.get_location("Bank 25,000,000 Coins")
    banked_coins_17 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", "Banked 1,000,000 Coins", "Banked 2,000,000 Coins", "Banked 10,000,000 Coins", count=15)
    world.set_rule(bank_coins_18, banked_coins_17)
    
    bank_coins_17 = world.get_location("Bank 10,000,000 Coins")
    banked_coins_16 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", "Banked 1,000,000 Coins", "Banked 2,000,000 Coins", count=14)
    world.set_rule(bank_coins_17, banked_coins_16)
    
    bank_coins_16 = world.get_location("Bank 2,000,000 Coins")
    banked_coins_15 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", "Banked 1,000,000 Coins", count=13)
    world.set_rule(bank_coins_16, banked_coins_15)
    
    bank_coins_15 = world.get_location("Bank 1,000,000 Coins")
    banked_coins_14 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", "Banked 500,000 Coins", count=12)
    world.set_rule(bank_coins_15, banked_coins_14)
    
    bank_coins_14 = world.get_location("Bank 500,000 Coins")
    banked_coins_13 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", "Banked 250,000 Coins", count=11)
    world.set_rule(bank_coins_14, banked_coins_13)
    
    bank_coins_13 = world.get_location("Bank 250,000 Coins")
    banked_coins_12 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", "Banked 100,000 Coins", count=10)
    world.set_rule(bank_coins_13, banked_coins_12)
    
    bank_coins_12 = world.get_location("Bank 100,000 Coins")
    banked_coins_11 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", "Banked 50,000 Coins", count=9)
    world.set_rule(bank_coins_12, banked_coins_11)
    
    bank_coins_11 = world.get_location("Bank 50,000 Coins")
    banked_coins_10 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", "Banked 25,000 Coins", count=8)
    world.set_rule(bank_coins_11, banked_coins_10)
    
    bank_coins_10 = world.get_location("Bank 25,000 Coins")
    banked_coins_9 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", "Banked 10,000 Coins", count=7)
    world.set_rule(bank_coins_10, banked_coins_9)
    
    bank_coins_9 = world.get_location("Bank 10,000 Coins")
    banked_coins_8 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", "Banked 5,000 Coins", count=6)
    world.set_rule(bank_coins_9, banked_coins_8)
    
    bank_coins_8 = world.get_location("Bank 5,000 Coins")
    banked_coins_7 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", "Banked 2,500 Coins", count=5)
    world.set_rule(bank_coins_8, banked_coins_7)
    
    bank_coins_7 = world.get_location("Bank 2,500 Coins")
    banked_coins_6 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", "Banked 1,000 Coins", count=4)
    world.set_rule(bank_coins_7, banked_coins_6)
    
    bank_coins_6 = world.get_location("Bank 1,000 Coins")
    banked_coins_5 = HasFromList("Banked 100 Coins", "Banked 250 Coins", "Banked 500 Coins", count=3)
    world.set_rule(bank_coins_6, banked_coins_5)
    
    bank_coins_5 = world.get_location("Bank 500 Coins")
    banked_coins_4 = HasFromList("Banked 100 Coins", "Banked 250 Coins", count=2)
    world.set_rule(bank_coins_5, banked_coins_4)
    
    bank_coins_4 = world.get_location("Bank 250 Coins")
    banked_coins_3 = HasFromList("Banked 100 Coins", count=1)
    world.set_rule(bank_coins_4, banked_coins_3)
    
    bank_coins_3 = world.get_location("Bank 100 Coins")
    banked_coins_2 = HasFromList("Banked 10 Coins", "Banked 25 Coins", count=2)
    world.set_rule(bank_coins_3, banked_coins_2)
    
    bank_coins_2 = world.get_location("Bank 25 Coins")
    banked_coins_1 = HasFromList("Banked 10 Coins", count=1)
    world.set_rule(bank_coins_2, banked_coins_1)
    
    
    bank_stars_10 = world.get_location("Bank 9,999 Stars")
    banked_stars_9 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", "Banked 250 Stars", "Banked 500 Stars", "Banked 1,000 Stars", "Banked 2,500 Stars", "Banked 5,000 Stars", count=9)
    world.set_rule(bank_stars_10, banked_stars_9)
    
    bank_stars_9 = world.get_location("Bank 5,000 Stars")
    banked_stars_8 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", "Banked 250 Stars", "Banked 500 Stars", "Banked 1,000 Stars", "Banked 2,500 Stars", count=8)
    world.set_rule(bank_stars_9, banked_stars_8)
    
    bank_stars_8 = world.get_location("Bank 2,500 Stars")
    banked_stars_7 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", "Banked 250 Stars", "Banked 500 Stars", "Banked 1,000 Stars", count=7)
    world.set_rule(bank_stars_8, banked_stars_7)
    
    bank_stars_7 = world.get_location("Bank 1,000 Stars")
    banked_stars_6 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", "Banked 250 Stars", "Banked 500 Stars", count=6)
    world.set_rule(bank_stars_7, banked_stars_6)
    
    bank_stars_6 = world.get_location("Bank 500 Stars")
    banked_stars_5 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", "Banked 250 Stars", count=5)
    world.set_rule(bank_stars_6, banked_stars_5)
    
    bank_stars_5 = world.get_location("Bank 250 Stars")
    banked_stars_4 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", "Banked 100 Stars", count=4)
    world.set_rule(bank_stars_5, banked_stars_4)
    
    bank_stars_4 = world.get_location("Bank 100 Stars")
    banked_stars_3 = HasFromList("Banked 10 Stars", "Banked 25 Stars", "Banked 50 Stars", count=3)
    world.set_rule(bank_stars_4, banked_stars_3)
    
    bank_stars_3 = world.get_location("Bank 50 Stars")
    banked_stars_2 = HasFromList("Banked 10 Stars", "Banked 25 Stars", count=2)
    world.set_rule(bank_stars_3, banked_stars_2)
    
    bank_stars_2 = world.get_location("Bank 25 Stars")
    banked_stars_1 = HasFromList("Banked 10 Stars", count=1)
    world.set_rule(bank_stars_2, banked_stars_1)
    

    # # For the final boss, we also need to chain multiple conditions.
    # # First of all, you always need a Sword and a Shield.
    # # So far, we used the | and & operators to chain "Has" rules.
    # # Instead, we can also use HasAny for an or-chain of items, or HasAll for an and-chain of items.
    # has_sword_and_shield: Rule = HasAll("Sword", "Shield")

    # # In hard mode, the player also needs both Health Upgrades to survive long enough to defeat the boss.
    # # For this, we can use the optional "count" parameter for "Has".
    # has_both_health_upgrades = Has("Health Upgrade", count=2)

    # # Previously, we used an "if world.options.hard_mode" condition to check if we should apply the extra requirement.
    # # However, if you're comfortable with boolean logic, there is another way.
    # # OptionFilter is a rule component which isn't a "Rule" on its own, but when used in a boolean expression with
    # # rules, it acts like True if the option has the specified value, and acts like False otherwise.
    # hard_mode_is_off = OptionFilter(HardMode, False)

    # # So with this option-checking rule component in hand, we can write our boss condition like this:
    # can_defeat_final_boss = has_sword_and_shield & (hard_mode_is_off | has_both_health_upgrades)
    # # If you're not as comfortable with boolean logic, it might be somewhat confusing why this is correct.
    # # There is nothing wrong with using "if" conditions to check for options, if you find that easier to understand.
    can_access_star_door = Has("Star Key") & CanReachRegion("Zone 5")

    # # Finally, we apply the rule to our "Final Boss Defeated" event location.
    # final_boss = world.get_location("Final Boss Defeated")
    # world.set_rule(final_boss, can_defeat_final_boss)
    
    open_star_door = world.get_location("Open Star Door")
    world.set_rule(open_star_door, can_access_star_door)


def set_completion_condition(world: BerryBuryBerryWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # For this, we can use world.set_completion_rule.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    # can_open_star_door: Rule = Has("Star Key") & CanReachLocation("Zone 5")

    # # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # # So lets undo what we just did, and instead set the completion condition to:
    world.set_completion_rule(Has("Victory"))


# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".
