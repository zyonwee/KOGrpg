import items as item
import KoGDAO.itemDAO as itemDao
import monsters as m
import Interfaces.pets as p
import KoGDAO.allPetsDAO as ap
stages = ["Baby", "In-Training", "Rookie", "Champion", "Ultimate", "Mega", "Ultra"]
attr = ["Neutral", "Fire", "Water", "Electric", "Dark", "Earth", "Wind", "Plant", "Light"]

def list_help(h):
    if h == "egg common":
        return "Hatch it with `kog use egg <name>` to get all Neutral Baby pets"
    if h == "egg uncommon":
        return "Hatch it with `kog use egg <name>` to get all random In-Training pets"

    if h == "attr" or h == "attribute":
        return "Attributes are the factors of evolution. A pet can only evolve to the next level with the same Attributes." \
               "\n\nNeutrals are differents, they can choose all Attribute route." \
               "\nAttribute : Neutral, Fire, Water, Electric, Dark, Earth, Wind, Plant, Light"

    if h == "realm" or h == "realms":
        return "Realm is incremental every 10 levels. The higher ur realms, the higher evolution ur pet can reach. More actions are also released for each realm!"

    if h == "evo" or h == "evolve" or h == "evolution":
        return "Evolution is based on Attributes. There are at least 7 tiers of evolution! You can only evolve when your trainger is in a high enough realm!" \
               "\nEvolve with `kog evolve` "

    if h == "core" or h == "necessary core":
        return "Do `kog shop pet` to buy a core. Or Craft them (unavailable now) !!"

    if h in item.get_all_item_exist_name_lower():
        print(h, item.get_all_item_exist_name_lower())
        return f"**{h.capitalize()} {itemDao.get_item_emoji(h)}**\n**Item Description:** {itemDao.get_desc(h)}" \
               f"\n**Item Type:** {itemDao.get_type(h)}"

    if h in item.get_all_monsters_exist_name_lower():
        print(h, item.get_all_monsters_exist_name_lower())
        return f"{h.capitalize()}\n**Description** :{m.get_desc(h)}"

    if "." in h:
        string = ""
        h = h.rsplit(".")
        # print(h[0].title(),h[1].title())
        if h[0].title() in attr:
            # print("attr")
            if h[1].title() in stages:
                # print("stg")
                h = ap.get_allattr_stage(h[0], h[1])
                string += "All Pets attributed to this stage are :"
                for i in h:
                    string += f" `{i}|{h[i]}` "
                return string
            else:
                return "Check if the format is `kog help [Attribute].[Stage]` \n\nFor more info Attributes  `kog help attr`"
        else:
            return "Check if the format is `kog help [Attribute].[Stage]` \n\nFor more info Attributes  `kog help attr`"

    if h.title() in stages or h.title() in attr:
        return "Check if the format is `kog help [Attribute].[Stage]` \n\nFor more info Attributes  `kog help attr`"

    if " " in h:
        h = h.rsplit(" ")
        if h[0].title() in stages or h[1].title() in attr:
            return "Check if the format is `kog help [Attribute].[Stage]` \n\nFor more info Attributes  `kog help attr`"

    elif h.title() in stages or h.title() in attr:
        return "Check if the format is `kog help [Attribute].[Stage]` \n\nFor more info Attributes  `kog help attr`"

    if h == "interface":
        return "`kog` `kog profile` `kog shop` `kog inv` `kog recipes`"\
                "\n\n`kog shop [egg|recipes|lb|pet]`\n\n`kog help <item name>`"

    if h == "action":
        return "`kog hunt` `kog heal` `kog craft` `kog use <number> <item name>`"

    if h == "shop":
        return "`kog buy <number> <name>` `kog sell <number> <name>`"

    if h == "pet":
        return "Do `kog use <name egg>` to hatch egg. Remember to set them as main with `kog main <name>`! You can see the detailed info with `kog pet <name>`.\n" \
               "\n\nTo evolve `kog evolve <name>` \n\n To level up `kog use <number> pet treats`\n\n`kog pet` `kog pets` `kog main <name>` `kog evolve <name>` \n\n`kog help [Attribute].[Stage]`" \
               "\n\n `kog help evo` `kog help core` `kog help necessary core` `kog help attr`"

    if h == "casino":
        return "`kog cf [h/t] [money]`"
