# Prompt Engineering Process

I grabbed code from the demo to get started

changed message content to "you are a DND dungeon master and must provide the a customizable character sheet" Failure

changed message content to "you are a DND dungeon master" Successful run


sign_your_name = 'Nicholas Novak'
model = 'llama3.2'
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 'You are a dungeon master'},
]


**Your Stats:**

* Strength: 12 (+1)
* Dexterity: 14 (+2)
* Intelligence: 10
* Wisdom: 16 (+3)
* Charisma: 12

**Your Equipment:**

* A short sword for close combat
* Leather armor for protection
* A backpack with provisions, a waterskin, and 10 days' worth of rations
* A holy symbol of your goddess, granting you access to divine magic

**Your Divine Magic:**

As a Cleric, you have access to the following spells:

* Healing Word (1st level): Restore 4d8 + Wisdom modifier hit points to a target.
* Shield of Faith (1st level): Grant yourself a boost to Armor Class for 1 minute.
* Bless (1st level): Give a target ally a bonus to attack and damage rolls for 1 minute.

**Your Starting Equipment**

You have the following items in your inventory:

* A short sword
* Leather armor
* Backpack with provisions, waterskin, and rations
* Holy symbol of your goddess
* Spell component pouch

This seems to produce a normal starter build for a cleric 

