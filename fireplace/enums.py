from enum import IntEnum


class CardType(IntEnum):
	INVALID = 0
	GAME = 1
	PLAYER = 2
	HERO = 3
	MINION = 4
	SPELL = 5
	ENCHANTMENT = 6
	WEAPON = 7
	ITEM = 8
	TOKEN = 9
	HERO_POWER = 10


class Race(IntEnum):
	INVALID = 0
	BLOODELF = 1
	DRAENEI = 2
	DWARF = 3
	GNOME = 4
	GOBLIN = 5
	HUMAN = 6
	NIGHTELF = 7
	ORC = 8
	TAUREN = 9
	TROLL = 10
	UNDEAD = 11
	WORGEN = 12
	GOBLIN2 = 13
	MURLOC = 14
	DEMON = 15
	SCOURGE = 16
	MECHANICAL = 17
	ELEMENTAL = 18
	OGRE = 19
	PET = 20
	TOTEM = 21
	NERUBIAN = 22
	PIRATE = 23
	DRAGON = 24

	# Alias for PET
	BEAST = 20


class GameTag(IntEnum):
	TURN = 20
	CURRENT_PLAYER = 23
	FIRST_PLAYER = 24
	RESOURCES_USED = 25
	RESOURCES = 26
	DEFENDING = 36
	PROPOSED_DEFENDER = 37
	ATTACKING = 38
	PROPOSED_ATTACKER = 39
	ATTACHED = 40
	EXHAUSTED = 43
	DAMAGE = 44
	HEALTH = 45
	ATK = 47
	COST = 48
	ZONE = 49
	CONTROLLER = 50
	OWNER = 51
	CARD_ID = 186
	DURABILITY = 187
	SILENCED = 188
	WINDFURY = 189
	TAUNT = 190
	STEALTH = 191
	SPELLPOWER = 192
	DIVINE_SHIELD = 194
	CHARGE = 197
	CARDRACE = 200
	FACTION = 201
	CARDTYPE = 202
	FREEZE = 208
	ENRAGED = 212
	RECALL = 215
	DEATHRATTLE = 217
	BATTLECRY = 218
	SECRET = 219
	COMBO = 220
	CANT_ATTACK = 227
	FROZEN = 260
	COMBO_ACTIVE = 266
	NUM_CARDS_PLAYED_THIS_TURN = 269
	ARMOR = 292
	MORPH = 293
	TEMP_RESOURCES = 295
	RECALL_OWED = 296
	NUM_ATTACKS_THIS_TURN = 297
	CANT_BE_TARGETED_BY_ABILITIES = 311
	SHOULDEXITCOMBAT = 312
	CREATOR = 313
	NUM_MINIONS_PLAYED_THIS_TURN = 317
	HEALTH_MINIMUM = 337
	OneTurnEffect = 338
	SILENCE = 339
	ImmuneToSpellpower = 349
	ADJACENT_BUFF = 350
	AURA = 362
	POISONOUS = 363
	TAG_AI_MUST_PLAY = 367
	NUM_MINIONS_PLAYER_KILLED_THIS_TURN = 368
	NUM_MINIONS_KILLED_THIS_TURN = 369
	AFFECTED_BY_SPELL_POWER = 370
	EXTRA_DEATHRATTLES = 371
	TOPDECK = 377
	FORGETFUL = 389

	# flavor
	ELITE = 114
	CARD_SET = 183
	CLASS = 199
	RARITY = 203
	Collectible = 321

	# unused
	SUMMONED = 205
	AttackVisualType = 251
	DevState = 268
	ENCHANTMENT_BIRTH_VISUAL = 330
	ENCHANTMENT_IDLE_VISUAL = 331
	InvisibleDeathrattle = 335  # Hack for Bigglesworth/Worshipper
	GrantCharge = 355  # RFG
	HealTarget = 361  # Northshire Cleric

	# strings
	TRIGGER_VISUAL = 32
	CARDTEXT_INHAND = 184
	CARDNAME = 185
	CardTextInPlay = 252
	TARGETING_ARROW_TEXT = 325
	ARTISTNAME = 342
	FLAVORTEXT = 351
	HOW_TO_EARN = 364
	HOW_TO_EARN_GOLDEN = 365

	# Renamed
	DEATH_RATTLE = 217


class PlayReq(IntEnum):
	REQ_MINION_TARGET = 1
	REQ_FRIENDLY_TARGET = 2
	REQ_ENEMY_TARGET = 3
	REQ_DAMAGED_TARGET = 4
	REQ_ENCHANTED_TARGET = 5
	REQ_FROZEN_TARGET = 6
	REQ_CHARGE_TARGET = 7
	REQ_TARGET_MAX_ATTACK = 8
	REQ_NONSELF_TARGET = 9
	REQ_TARGET_WITH_RACE = 10
	REQ_TARGET_TO_PLAY = 11
	REQ_NUM_MINION_SLOTS = 12
	REQ_WEAPON_EQUIPPED = 13
	REQ_ENOUGH_MANA = 14
	REQ_YOUR_TURN = 15
	REQ_NONSTEALTH_ENEMY_TARGET = 16
	REQ_HERO_TARGET = 17
	REQ_SECRET_CAP = 18
	REQ_MINION_CAP_IF_TARGET_AVAILABLE = 19
	REQ_MINION_CAP = 20
	REQ_TARGET_ATTACKED_THIS_TURN = 21
	REQ_TARGET_IF_AVAILABLE = 22
	REQ_MINIMUM_ENEMY_MINIONS = 23
	REQ_TARGET_FOR_COMBO = 24
	REQ_NOT_EXHAUSTED_ACTIVATE = 25
	REQ_UNIQUE_SECRET = 26
	REQ_TARGET_TAUNTER = 27
	REQ_CAN_BE_ATTACKED = 28
	REQ_ACTION_PWR_IS_MASTER_PWR = 29
	REQ_TARGET_MAGNET = 30
	REQ_ATTACK_GREATER_THAN_0 = 31
	REQ_ATTACKER_NOT_FROZEN = 32
	REQ_HERO_OR_MINION_TARGET = 33
	REQ_CAN_BE_TARGETED_BY_SPELLS = 34
	REQ_SUBCARD_IS_PLAYABLE = 35
	REQ_TARGET_FOR_NO_COMBO = 36
	REQ_NOT_MINION_JUST_PLAYED = 37
	REQ_NOT_EXHAUSTED_HERO_POWER = 38
	REQ_CAN_BE_TARGETED_BY_OPPONENTS = 39
	REQ_ATTACKER_CAN_ATTACK = 40
	REQ_TARGET_MIN_ATTACK = 41
	REQ_CAN_BE_TARGETED_BY_HERO_POWERS = 42
	REQ_ENEMY_TARGET_NOT_IMMUNE = 43
	REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY = 44
	REQ_MINIMUM_TOTAL_MINIONS = 45
	REQ_MUST_TARGET_TAUNTER = 46
	REQ_UNDAMAGED_TARGET = 47
	REQ_CAN_BE_TARGETED_BY_BATTLECRIES = 48
	REQ_STEADY_SHOT = 49
	REQ_MINION_OR_ENEMY_HERO = 50
	REQ_DRAG_TO_PLAY = 51


class Rarity(IntEnum):
	INVALID = 0
	COMMON = 1
	FREE = 2
	RARE = 3
	EPIC = 4
	LEGENDARY = 5


class SpellZoneTag(IntEnum):
	NONE = 0
	PLAY = 1
	HERO = 2
	HERO_POWER = 3
	WEAPON = 4
	DECK = 5
	HAND = 6
	GRAVEYARD = 7
	SECRET = 8


class Zone(IntEnum):
	INVALID = 0
	PLAY = 1
	DECK = 2
	HAND = 3
	GRAVEYARD = 4
	REMOVEDFROMGAME = 5
	SETASIDE = 6
	SECRET = 7
