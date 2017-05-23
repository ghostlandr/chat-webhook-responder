"""
Definition webhook responder
"""
import logging

from app.responders.slack import SlackResponder
from settings import DNDFINE_TOKENS


class DndefineResponder(object):
    """ Define a word! """
    KEY_WORD = 'dndfine'
    TOKENS = DNDFINE_TOKENS

    def get_definitions(self, term):
        logging.info(u'Searching checking dict for term: %s', term)
        if term.lower() == "list":
            return self._format_response(term, u', '.join(DEFINITIONS.iterkeys()))
        term = term.replace(" ", "_")
        return self._format_response(term, DEFINITIONS.get(term.lower()))

    @staticmethod
    def _format_response(term, definition):
        response = u''

        response += u'*{}*\n\n'.format(term)

        if definition:
            response += u'' + definition + u'\n'
        else:
            response += u'There aren\'t any definitions for {} yet.'.format(term)

        return response

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))


class DndefineSlackResponder(DndefineResponder, SlackResponder):
    """
    Responds to /udefine/slack/ requests
    """


DEFINITIONS = {
    'list': 'Lists all the definitions currently available',
    'initiative': 'Roll 1d20 + dex modifier',
    'modifier_table': "```\nAbility Scores and Modifiers\nScore Modifier\n\n1        -5 \n2-3      -4 \n4-5      -3 \n6-7      -2 \n8-9      -1 \n10-11    +0 \n12-13    +1 \n14-15    +2\n16-17    +3 \n18-19    +4\n20-21    +5 \n22-23    +6 \n24-25    +7 \n26-27    +8 \n28-29    +9\n30       +10\n```",
    'darkvision': 'Half-Orc/Tiefling: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light',
    'relentless_endurance': 'Half-Orc: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You cant use this feature again until you finish a long rest.',
    'savage_attacks': 'Half-Orc: When you score a critical hit with a melee weapon attack, you can roll one of the weapons damage dice one additional time and add it to the extra damage of the critical hit',
    'hellish_resistance': 'Tiefling: You have resistance to fire damage.',
    'infernal_legacy': 'You know the thaumaturgy cantrip. Once you reach 3rd level, you can cast the hellish rebuke spell once per day as a 2nd-level spell. Once you reach 5th level, you can also cast the darkness spell once per day. Charisma is your spellcasting ability for these spells.',
    'fighter': 'A master of martial combat, skilled with a variety o f weapons and armor.\n Hit Die: d10\n Saving Throw Proficiencies: STR & DEX\nArmor and Weapon Proficiencies: All armor, shields, simple and martial weapons',
    'ranger': 'A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization \n Hit Die: d10\n Saving Throw Proficiencies: STR & DEX\n Armor and Weapon Proficiencies: Light and medium armor, shields, simple and martial weapons',
    'warlock': 'A wielder of magic that is derived from a bargain with an extraplanar entity. \n Hit Die: d6\n Saving Throw Proficiencies: INT & WIS\n Armor and Weapon Proficiencies: Light armor, simple weapons',
    'fighting_style_protection': 'Fighter: When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.',
    'second_wind': 'Fighter: You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again.',
    'favored_enemy': 'Ranger: Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.',
    'natural_explorer': 'You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. \nWhen you make an Intelligence or Wisdom check related to your favored terrain,your proficiency bonus is doubled if you are using a skill that youre proficient in.\n\nWhile traveling for an hour or more in your favored terrain, you gain the following benefits:\n- Difficult terrain doesnt slow your groups travel.\n- Your group cant becom e lost except by magical means.\n- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n- If you are traveling alone, you can move stealthily at a normal pace.\n- When you forage, you find twice as much food as you normally would.\n- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.',
    'warlock_spellcasting_ability': 'Charisma is your spellcasting ability for your warlock spells, so you use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.\n Spell save DC = 8 + your proficiency bonus + your Charisma modifier\n Spell attack modifier = your proficiency bonus + your Charisma modifier',
    'advantage': 'Roll a second d20 when you make the roll and choose the higher of the 2 numbers',
    'disadvantage': 'Roll a second d20 when you make the roll and choose the lower of the 2 numbers',
    'difficulty_classes': '```Typical Difficulty Classes\nTask Difficulty      DC\nVery easy            5\nEasy                 10 \nMedium               15\nHard                 20 \nVery hard            25\nNearly impossible    30```',
    'skills': '\n*Strength*\nAthletics\n*Dexterity*\nAcrobatics\nSleight of Hand\nStealth\n*Intelligence*\nArcana\nHistory\nInvestigation\nNature\nReligion\n*Wisdom*\nAnimal Handling\nInsight\nMedicine\nPerception\nSurvival\n*Charisma*\nDeception\nIntimidation\nPerformance\nPersuasion',
    'fall_damage': '1d6 bludgeoning damage for every 10 feet it fell, to a maximum of 20d6.',
    'suffocating': 'A creature can hold its breath for a number of minutes equal to 1 + its Constitution modifier (minimum of 30 seconds). \nWhen a creature runs out of breath, it can survive for a number of rounds equal to its Constitution modifier (minimum 1 round). At the start of its next turn, it drops to 0 hit points and is dying',
    'short_rest': 'At least 1 hour long. \n A character can spend one or more Hit Dice at the end of a short rest, up to the characters maximum number of Hit Dice, which is equal to the characters level. \nFor each Hit Die spent in this way, the player rolls the die and adds the characters Constitution modifier to it. The character regains hit points equal to the total. The player can decide to spend an additional Hit Die after each roll. A character regains some spent Hit Dice upon finishing a long rest.',
    'long_rest': 'At least 8 hours long.\n At the end of a long rest, a character regains all lost hit points. The character also regains spent Hit Dice, up to a number of dice equal to half of the characters total number of them. For example, if a character has eight Hit Dice, he or she can regain four spent Hit Dice upon finishing a long rest.\n A character cant benefit from more than one long rest in a 24-hour period, and a character must have at least 1 hit point at the start of the rest to gain its benefits.',
    'combat_steps': '1. Determine surprise\n2. Establish positions\n3. Roll initiative\n4. Take turns\n5. Begin the next round',
    'combat_turn': 'In any order: Move, Action, Free Action, Possibly Bonus Action',
    'combat_free_actions': 'Short speach, interact with one item',
    'combat_actions': 'Attack, Cast a spell, Dash, Disengage, Dodge, Help, Hide, Ready, Search, Use Object',
    'attack': 'Roll Attack, Roll damage on hit',
    'cast_spell': 'Do what spell says, might take multiple actions',
    'dash': 'double your movement',
    'disengage': 'Your movement doesnt provoke opportunity attacks for the rest of the turn.',
    'dodge': 'Until the start of your next turn, any attack roll made against you has disadvantage if you can see the attacker, and you make Dexterity saving throws with advantage',
    'help': '1. The creature you aid gains advantage on the next ability check it makes to perform the task you are helping with. \nOr\n2. you can aid a friendly creature in attacking a creature within 5 feet of you. You feint, distract the target, or in some other way team up to make your allys attack more effective. If your ally attacks the target before your next turn, the first attack roll is made with advantage.',
    'hide': 'You make a Dexterity (Stealth) check in an attempt to hide, following the rules in chapter 7 for hiding',
    'ready': 'Specify a trigger and when that happens you can act later in the round using your reaction.',
    'search': 'You devote your attention to finding something. Depending on the nature of your search, the DM might have you make a W isdom (Perception) check or an Intelligence (Investigation) check.',
    'use_object': 'You normally interact with an object while doing something else, such as when you draw a sword as part of an attack. When an object requires your action for its use, you take the Use an Object action. This action is also useful when you want to interact with more than one object on your turn.',
    'melee_attack': '1d20 + STR + proficiency',
    'ranged_attack': '1d20 + DEX + proficiency',
    'spell_attack': "1d20 + Spell Casting Ability + proficiency",
    'ranged_in_close': 'When you make a ranged attack with a weapon, a spell, or some other means, you have disadvantage on the attack roll if you are within 5 feet of a hostile creature who can see you and who isnt incapacitated.',
    'opportunity_attack': 'You can make an opportunity attack when a hostile creature that you can see moves out of your reach.',
    'cover': 'A target with half cover has a +2 bonus to AC and Dexterity saving throws.\nA target with three-quarters cover has a +5 bonus to AC and Dexterity saving throws.\nA target with total cover cant be targeted directly by an attack or a spell.',
    'critical_hit': 'When you score a critical hit, you get to roll extra dice for the attacks damage against the target. Roll all of the attacks damage dice twice and add them together. Then add any relevant modifiers as normal.',
    'damage_types': '*Bludgeoning* . Blunt force attacks-hammers, falling, constriction, and the like-deal bludgeoning damage.\n *Cold* . The infernal chill radiating from an ice devils spear and the frigid blast of a white dragons breath deal cold damage.\n *Fire* . Red dragons breathe fire, and many spells conjure flames to deal fire damage.\n *Force* . Force is pure magical energy focused into a damaging form. Most effects that deal force damage are spells, including magic missile and spiritual weapon.\n *Lightning* . A lightning bolt spell and a blue dragons breath deal lightning damage.\n *Necrotic* . Necrotic damage, dealt by certain undead and a spell such as chill touch, withers matter and even the soul.\n *Piercing* . Puncturing and impaling attacks, including spears and monsters bites, deal piercing damage.\n *Poison* . Venomous stings and the toxic gas of a green dragons breath deal poison damage.\n *Psychic* . Mental abilities such as a mind flayers psionic blast deal psychic damage.\n *Radiant* . Radiant damage, dealt by a clerics flame strike spell or an angels smiting weapon, sears the flesh like fire and overloads the spirit with power.\n *Slashing* . Swords, axes, and monsters claws deal slashing damage.\n *Thunder* . A concussive burst of sound, such as the effect of the thunderwave spell, deals thunder damage.',
    'instant_death': 'Massive damage can kill you instantly. When damage reduces you to 0 hit points and there is damage remaining, you die if the remaining damage equals or exceeds your hit point maximum.',
    'unconscious': 'If damage reduces you to 0 hit points and fails to kill you, you fall unconscious (see appendix A). This unconsciousness ends if you regain any hit points.',
    'death_saving_throw': 'At the start of your turn, 1d20 no modifiers. <10 is a failure. 3 failures you die, 3 success you are stabilized, 1 = 2 failures, 20 = 2 successes. Damage taken counts as a failure.',
    'stabalizing': '1d20 + WIS (medicine) vs DC 10',
    'blade_ward': 'Cantrip\nCasting Time: 1 action\nRange: self\nComponents: V, S\nDuration: 1 round\nDescription: You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks.',
    'eldritch_blast': 'Cantrip\nCasting Time: 1 action\nRange 120ft\nComponenets: V, S\nDuration: instantaneous\nDescription: A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1dlO force damage. The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.',
    'witch_bolt': '1st level Spell\nCasting Time: 1 action\nRange: 30ft\nComponents: V, S, M\nDuration: Concentration, up to 1 min\nDescription:  beam of crackling, blue energy lances out toward a creature within range, forming a sustained arc of lightning between you and the target. Make a ranged spell attack against that creature. On a hit, the target takes 1d12 lightning damage, and on each of your turns for the duration, you can use your action to deal 1d12 lightning damage to the target automatically. The spell ends if you use your action to do anything else. The spell lso ends if the target is ever outside the spells range or if it has total cover from you.\nAt HigherLevels. When you cast this spell using a spell slot of 2nd level or higher, the initial damage increases by 1d12 for each slot level above 1st.',
    'arms_of_hadar': '1st level Spell\nCasting Time: 1 action\nRange: Self (10-foot radius)\nComponents: V, S\nDuration: Instantaneous\nDescription: You invoke the power of Hadar, the Dark Hunger. Tendrils of dark energy erupt from you and batter all creatures within 10 feet of you. Each creature in that area must make a Strength saving throw. On a failed save, a target takes 2d6 necrotic damage and cant take reactions until its next turn. On a successful save, the creature takes half damage, but suffers no other effect.\nAtHigherLevels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.',
    'thaumaturgy': 'Cantrip\nCasting Time: 1 action\nRange: 30ft\nComponents: V\nDuration: Up to 1 minute\nDescription: You manifest a minor wonder, a sign of supernatural power, within range. You create one of the following magical effects within range:\n- Your voice booms up to three times as loud as normal for 1 minute.\n- You cause flames to flicker, brighten, dim, or change color for 1 minute.\n- You cause harmless tremors in the ground for 1 minute.\n- You create an instantaneous sound that originates from a point of your choice within range, such as a rumble of thunder, the cry of a raven, or ominous whispers.\n- You instantaneously cause an unlocked door or win  dow to fly open or slam shut.\n- You alter the appearance of your eyes for 1 minute.\nIf you cast this spell multiple times, you can have up to three of its 1-minute effects active at a time, and you can dismiss such an effect as an action.',
    'burning_hands': '1st level Evocation\nCasting Time: 1 action\nRange: Self (15-foot cone)\nComponents: V, S\nDuration: Instantaneous\nDescription: As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one. \nThe fire ignites any flammable objects in the area that arent being worn or carried.',
    'action_surge': 'Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action. Once you use this feature, you must finish a short or long rest before you can use it again.',
    'fiendish_vigor': 'You can cast false life on yourself at will as a 1st-level spell, without expending a spell slot or material com ponents.',
    'agonizing_blast': '_Prerequisite: eldritch blast cantrip_\nWhen you cast eldritch blast, add your Charisma modifier to the damage it deals on a hit.',
    'false_life': '1st level necromancy\nCasting Time: 1 action\nRange: self\nComponents: V, S, M\nDuration: 1 hour\nDescription: Bolstering your self with a necromantic facsimile of life, you gain 1d4+4 temporary hitpoints for the duration.\nAt Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you gain 5 additional temporary hit points for each slot level above 1st.',
    'spell_slot': 'Regardless of how many spells a caster knows or prepares, he or she can cast only a limited number of spells before resting. Spell slots represent the number (and power) of spells a caster can cast between long rests',
    'grappling': 'The target of your grapple must be no more than one size larger than you, and it must be within your reach. Using at least one free hand, you try to seize the target by making a grapple check, a Strength (Athletics) check contested by the targets Strength (Athletics) or Dexterity (Acrobatics) check (the target chooses the ability to use). If you succeed, you subject the target to the grappled condition',
    'escape_grapple': 'A grappled creature can use its action to escape. To do so, it must succeed on a Strength (Athletics) or Dexterity (Acrobatics) check contested by your Strength (Athletics) check',
    'grapple_condition': '- A grappled creatures speed becom es 0, and it cant benefit from any bonus to its speed\n- The condition ends if the grappler is incapacitated \n -The condition also ends if an effect rem oves the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell',
    'temporary_hit_points': 'Temporary hit points arent actual hit points; they are a buffer against damage, a pool of hit points that protect you from injury.\nWhen you take damage, the temporary hit points are lost first.\nHealing cant restore temporary hit points, and they cant be added together',
    'archery': 'Ranger: You gain a +2 bonus to attack rolls you make with ranged weapons.',
    'cure_wounds': '1st level evocation\nCasting Time: 1 action\nRange: touch\nComponents: V,S\nDuration: Instantaneous\nDescription: A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.',
    'hunters_mark': '1st level divination\nCasting Time: 1 bonus Action\nRange: 90 feet\nComponents: V\nDuration: Concentration, up to 1 hour\nDescription: You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature.',
}
