def class_description(class_name):
    descriptions = {
            "Alchemist": """
Alchemists are masters in the use of potions, tinctures, poisons and admixtures. They excel in the use of simple weapons, but prefer a ranged approach rather than a melee role, as they have fairly low hit points and can only wear robes. As such they are quite adept at using simple throwing weapons such as daggers and darts. Alchemists are quite versatile, as they can use curative admixtures to heal both living and undead allies, have a wide variety of spell-like flasks that deal magical damage upon contact with their enemies, turn them into statues of gold or cover them in sticky glue. They also have the ability to coat their weapons in various poisons and magical imbues. Alchemists have a special method for using their abilities and spells, being able to change their preferred party role with three different stances in a complex, but rewarding, reaction and combination system.

The primary attribute of the Alchemist is Intelligence, but Dexterity should not be ignored for those who wish to pursue a ranged role in combat.

The Alchemist class can be purchased in the DDO Store for 1,495 DP and is free to VIP accounts. It is also available to 2018 Season Pass holders.""",
            "Artificer": """
Artificers combine magic with weapon technology and skill. Traditionally, Artificers prefer to avoid getting their hands dirty in a fight, using personally-made constructs to perform a variety of tasks, but are especially capable in combat. Artificers are jacks-of-all-trades: they can serve as backup healers, as competent offensive spellcasters and as both ranged & melee combatants; they can also find/disable traps and open locks plus have excellent supportive abilities. Artificers are the only class that can gain the use of Rune Arms.

The primary attributes of the Artificer are Dexterity and Intelligence.

The Artificer class must either be purchased in the DDO store for 995 DP or unlocked on a per-server basis by earning 150 House Cannith favor on a single character.
            """,
            "Barbarian": """
Barbarians are warriors who have special powers when enraged and specialise in dealing heavy damage. Barbarians wear less armor than fighters or paladins, but have more hit points and some innate damage reduction. Uncanny Dodge allows them to have a high dodge chance and excellent reflex saves in short bursts. While many Barbarian abilities are geared towards melee combat, they can also make passable ranged combatants should the need arise.

The primary attributes of the Barbarian are Strength and Constitution.
            """,
            "Bard": """
Bards possess many skills with some special spell casting ability. They can fulfil almost any role within a party. The primary draw of Bards is their ability to use songs to inspire and buff a party, providing small but stacking bonuses to many aspects of gameplay, such as weapon damage, spell effectiveness, dodge and armor class. Their spell lists contains mix of both divine and arcane, but are considered arcane overall: they can use spells focused on crowd control, healing and buffs, as well as offensive sonic spells that can daze or stun opponents. Bards can also learn Use Magic Device as a class skill, letting them easily operate any kind of magical item. They have been called the "best sixth man" because, with bard to fill the final party slot, their powerful musical buffs can boost five other players. Bards can deal significant damage when specced for either physical or magical combat and their respectable healing abilities assist the main healer in keeping the party alive. Bards also possess one of the few abilities in the game that can replenish spell points.

The primary attribute of the Bard is Charisma.
            """,
            "Cleric": """
Clerics are divine spell casters who specialise in healing and defence spells as well as some offensive ability in the way of light, fire, and physical spells. Many people think of clerics when looking for a healer, as Clerics have an enhancement tree devoted entirely to healing and support. Clerics can use any armor without penalty but are only proficient with Simple Weapons. Clerics can take up a melee weapon and dish out respectable damage, but they are not as capable as the more physical-based classes. They gain access to clerical domains at level 2, giving them great versatility in allowing them to specialise in certain aspects of the divine arts.

The primary attributes of the Cleric are Wisdom, determining maximum spell points and spellcasting effectiveness, and Charisma, impacting both the ability to Turn Undead and the number of uses of this ability.
            """,
            "Druid": """
Druids are divine spellcasters with a variety of offensive and supportive spells, but they are the epitome of crowd control and can fulfil that role regardless of their specialisation. They can be excellent melee combatants, able to use Wild Shape to transform into bears (strong and hardy tanks) and wolves (fast and agile attackers), or can take up a spellcasting role, turning into fire or water elementals to unleash primal forces of nature in the form of blizzards, thunderstorms, and earthquakes. Druids make strong solo characters considering their melee and self-healing options, especially at low and mid levels. Druids cannot use metal armor or wield metal shields; doing so removes their ability to use many of their druidic abilities.

The primary attribute of the Druid is Wisdom, determining maximum spell points and spellcasting effectiveness. Druids engaging in melee combat also make use of Strength and Constitution, determining hit chance, physical damage, and hit points. Druids get several bonuses to Strength and Constitution from their rage, and can amplify these bonuses with enhancements in Nature's Protector.
            """,
            "Favored Soul": """
Favored Souls are divine casters that follow a path similar to the Cleric. They have fewer spells at their disposal than clerics, being unable to change spell selection at Rest Shrines or in Taverns, but receive almost twice the number of spell points, enabling them to cast their spells more often. Favoured Souls gain energy resistance and inherent Damage Reduction as they progress. They can use light or medium armor proficiency with simple weapons, but gain the use of additional weapons based on their chosen God and can become capable melee combatants. They tend to be more focused on offense than support.

The primary attribute of the Favored Soul is the highest of either their Wisdom or Charisma. This is used for determining both maximum spell points and spell casting effectiveness. Wisdom or Charisma can also be used for hit and damage (if higher than Strength) when using their God's favored weapon.

The Favored Soul class must either be purchased in the DDO store for 995 DP or unlocked on a per-server basis by earning 2,500 Total Favor on a single character.
            """,
            "Fighter": """
Fighters are warriors with many extra feats (1 +1 every 2 levels up to 11), allowing them to specialise their role in martial combat. There are many ways to fight: single-weapon, two-handed, dual-wielding, a sword & shield or with a bow (or other ranged weapons)... you name it, a fighter can specialise in it. For best effect, players should thoroughly examine the feats they plan to select before creating this versatile front-line class. Fighters gain access to many unique feats that increase their offensive power, their defences and their ability to use tactical manoeuvres (such as Improved Trip, Improved Sunder or Stunning Blow).

The primary attributes of the Fighter, depending on the martial path they wish to follow, are Strength, Constitution and Dexterity (in varying amounts).
            """,
            "Monk": """
Monks are combatants that perform amazing techniques in battle by using an inner power source called ki. To use their special abilities, monks must be centered and remain in a state of physical and mental balance. To remain centered, a monk must be unencumbered, wielding monk-specific weapons or unarmed, and wear no armor except for robes and outfits. When not centered, monks lose the majority of their special bonuses. While their base weapon selectionis limited, monks can gain specialised training through feats and class enhancements to enable other weapons to be used while centered. They gain a variety of special feats as they increase in level. They can have extremely high Dodge and, at high levels, have a higher base movement speed than any other class.

The primary attribute of the Monk is Wisdom, which is used in retaining ki, increasing Armor Class and increasing the effectiveness of ki attacks and monk-specific tactical abilities. Strength, Constitution and Dexterity are also important.
            """,
            "Paladin": """
Paladins are warriors that trade some of their melee power for the ability to cast divine spells. Paladins often have the best saving throws of any character and gain immunity to fear and disease. They may serve as backup healers for short encounters and have passive auras that aid their party members when facing evil creatures. Paladins make great defensive characters, but can easily perform well in an offensive role with weapons.

The primary attributes of the Paladin are Wisdom, determining maximum spell points and spellcasting effectiveness, and Charisma, providing higher saves and increasing the effectiveness of their unique abilities. Strength and Constitution are also important, as the Paladin is a martial class.
            """,
            "Ranger": """
Rangers are inherently both archers and a dual-wielding melee class, being proficient in both combat styles. Rangers are capable of stealth combat, although not as effectively as Rogues, and can cast from a limited selection of divine spells. Rangers increase their damage with Favored Enemy feats, which let them pick up to five kinds of monsters to specialise in fighting, providing damage bonuses against those types that stack as they level up.

The primary attribute of the spellcasting Ranger is Wisdom, determining maximum spell points and spellcasting effectiveness. Strength and Dexterity are important for combat, increasing damage and accuracy with weapons.
            """,
            "Rogue": """
Rogues get more skill points in DDO than any other class. They are capable of finding/disarming traps and opening locks. Rogues can also deal devastating sneak attack damage when they are beneath the notice of their enemies - they are the best class for stealth and sneaking around. Rogues' defences are quite low, even though they have Evasion and a fairly high Dodge, so must rely on their wits and cunning to survive tough battles. Rogues can do well as either melee or ranged characters.

The primary attributes of the Rogue are Dexterity and Intelligence.
            """,
            "Sorcerer": """
Sorcerers are arcane spellcasters, who serve as the primary offensive magic class in DDO, but are physically quite weak. Sorcerer enhancements are built almost entirely around dealing significant elemental damage with spells. They have fewer spells at their disposal than Wizards, being unable to change spell selection at Rest Shrines or in Taverns, but can cast spells much faster than any other class and, often, have more maximum spell points than other classes, enabling them to cast their spells more often per Rest Shrine without using consumables, temporary spell points, Reaper mode Lost Souls, or other means to restore or preserve spell points.

The primary attribute of the Sorcerer is Charisma, determining maximum spell points and spellcasting effectiveness.
            """,
            "Warlock": """
Warlocks are arcane spellcasters who form pacts with powerful beings to gain power and magic, often seeking out rare and forbidden knowledge. They deal moderate amounts of damage with their Eldritch Blast but they do not require spell points to do so, ensuring a steady stream of magic damage at no cost. Warlocks have limited offensive magic but do have a variety of buffing, crowd control and utility spells. While Warlocks have moderate defences against physical attacks, they can defend against magical spells better than most other classes.

The primary attribute of the Warlock is Charisma, determining maximum spell points and spellcasting & eldritch blast effectiveness.
            """,
            "Wizard": """
Wizards are adaptive and versatile arcane casters, who gain five extra feats as they level to further enhance their spellcasting. Wizards have more spells available to them than Sorcerers do, being able to change spell selection at Rest Shrines or in Taverns, ensuring they always have the right spell(s) for the job. They do not, however, have as many starting spell points as Sorcerers. Wizards often perform as DC Casters', focusing on spells that instantly kill, control, charm, debuff or otherwise disable/weaken enemies, rather than direct damage spells.

The primary attribute of the Wizard is Intelligence, determining maximum spell points and spellcasting effectiveness.
            """
    }

    return descriptions[class_name]
