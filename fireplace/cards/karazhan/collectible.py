from ..utils import *

##
# Minions

class KAR_005:
	"Kindly Grandmother"
	deathrattle = Summon(CONTROLLER, "KAR_005a")

class KAR_006:
	"Cloaked Huntress"
	update = Refresh(FRIENDLY_HAND + SECRET, {GameTag.COST: SET(0)})

class KAR_009:
	"Babbling Book"
	play = Give(CONTROLLER, RandomSpell())

class KAR_010:
	"Nightbane Templar"
	powered_up = HOLDING_DRAGON
	play = powered_up & (Summon(CONTROLLER, "KAR_010a") * 2)

class KAR_021:
	"Wicked Witchdoctor"
	events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, RandomTotem()))

class KAR_029:
	"Runic Egg"
	deathratter = Draw(CONTROLLER)

class KAR_030a:
	"Pantry Spider"
	play = Summon(CONTROLLER, 'KAR_030')

class KAR_033:
	"Book Wyrm"
	powered_up = HOLDING_DRAGON, Find(ENEMY_MINIONS + (ATK <= 3))
	play = HOLDING_DRAGON & Destroy(TARGET)

class KAR_035:
	"Priest of the Feast"
	events = OWN_SPELL_PLAY.on(Heal(FRIENDLY_HERO, 3))

class KAR_036:
	"Arcane Anomaly"
	events = OWN_SPELL_PLAY.on(Buff(SELF, "KAR_036e"))

KAR_036e = buff(health=1)

# class KAR_037:
# 	"Avian Watcher"


# class KAR_041:
# 	"Moat Lurker"


# class KAR_044:
# 	"Moroes"


# class KAR_057:
# 	"Ivory Knight"


# class KAR_061:
# 	"The Curator"


# class KAR_062:
# 	"Netherspite Historian"


# class KAR_065:
# 	"Menagerie Warden"


# class KAR_069:
# 	"Swashburglar"


# class KAR_070:
# 	"Ethereal Peddler"


# class KAR_089:
# 	"Malchezaar's Imp"


# class KAR_092:
# 	"Medivh's Valet"


# class KAR_094:
# 	"Deadly Fork"


# class KAR_095:
# 	"Zoobot"


# class KAR_096:
# 	"Prince Malchezaar"


# class KAR_097:
# 	"Medivh, the Guardian"


# class KAR_114:
# 	"Barnes"


# class KAR_114e:


# class KAR_204:
# 	"Onyx Bishop"


# class KAR_205:
# 	"Silverware Golem"


# class KAR_702:
# 	"Menagerie Magician"


# class KAR_710:
# 	"Arcanosmith"


# class KAR_711:
# 	"Arcane Giant"


# class KAR_712:
# 	"Violet Illusionist"

##
# Spells

# class KAR_004:
# 	"Cat Trick"

# class KAR_013:
# 	"Purify"

# class KAR_025:
# 	"Kara Kazham!"

# class KAR_026:
# 	"Protect the King!"

# class KAR_073:
# 	"Maelstrom Portal"

# class KAR_075:
# 	"Moonglade Portal"

# class KAR_076:
# 	"Firelands Portal"

# class KAR_077:
# 	"Silvermoon Portal"

# class KAR_091:
# 	"Ironforge Portal"

##
# Weapons

# class KAR_028:
# 	"Fool's Bane"

# class KAR_063:
# 	"Spirit Claws"
