"""
The IdleRPG Discord Bot
Copyright (C) 2018-2020 Diniboy and Gelbpunkt
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import secrets

from typing import Dict, Union

items = [
    ("Punjabi Remix", 9500),
    ("Cold Shower", 8406),
    ("Hot Coffee", 7416),
    ("Unenriched Uranium", 9999),
    ("Wetstone", 2400),
    ("Bandit Essence", 1544),
    ("Catharsis", 9463),
    ("Cathartic Sacrifice", 10000),
    ("Leaf Blower", 150),
    ("Happy Noises", 274),
    ("Smelly Durian", 110),
    ("Vibranium", 6974),
    ("The Eternal Flesh", 8196),
    ("The Locksmith's Key", 7519),
    ("Flying Bullet", 4471),
    ("Nasty Roots", 3603),
    ("Psycadelic Mushrooms", 408),
    ("Smitten Dandruff", 505),
    ("Cute Kittens", 1337),
    ("Lots Of Cats", 7331),
    ("Wine Bottle", 105),
    ("Random Sheep", 375),
    ("Golden Nugget", 1009),
    ("Shiny Nickel", 196),
    ("White Crimson", 604),
    ("Lucky Penny", 706),
    ("Cinderellas Shoe", 126),
    ("Charged Quartz", 676),
    ("Rapunzel's Locks", 779),
    ("Kek's Laptops", 6004),
    ("Warrior's Scalp", 2004),
    ("Evangelion", 9098),
    ("Self-Purity", 1067),
    ("Plastic Memories", 1046),
    ("Ability To Feel", 10000),
    ("Sense Of Affection", 8994),
    ("Childhood Innocence", 7095),
    ("Cherished Memories", 6013),
    ("Phoenix Feather", 777),
    ("Excalibur", 9954),
    ("Saber Fang", 1016),
    ("Lion Tooth", 503),
    ("Dragon Claw", 5996),
    ("Spirits", 7995),
    ("Phoenix Feather", 1024),
    ("Cursed Parrot", 1464),
    ("Dragon Heartstring", 8099),
    ("Spiritual Birb", 5421),
    ("Power Stone", 6421),
    ("Time Stone", 5063),
    ("Soul Stone", 4134),
    ("Tiger Claws", 9412),
    ("Eagle Wings", 1644),
    ("Frog", 100),
    ("John Cena", 10000),
    ("Rabbit's Foot", 120),
    ("Cyclop's Eye", 470),
    ("Gold Pot", 2510),
    ("Goblin Stone", 1900),
    ("Dwarf Hat", 707),
    ("Unbreaking 3 Diamond Pickaxe", 8610),
    ("Ivory Needle", 253),
    ("Noodle Brain", 330),
    ("Maiden By The Water", 3005),
    ("Lover's Limb", 1010),
    ("Bran Just Bran", 5960),
    ("Beans", 100),
    ("Master Ball", 339),
    ("Master Sword", 604),
    ("Pepper", 105),
    ("Discarded Remenants", 180),
    ("Sugar", 103),
    ("Salt", 102),
    ("Bible", 777),
    ("Holy Water", 168),
    ("Holy Cross", 199),
    ("Holy Shit", 255),
    ("Holy Corpse", 321),
    ("Morning Coffee Cup", 109),
    ("The Gilded Grave", 222),
    ("Warm Blanket", 239),
    ("Bejeweled Egg", 3051),
    ("Zerekiel's Claw", 9946),
    ("Heart Of Zerekiel", 9999),
    ("Unwavering Gaze", 1001),
    ("Cobblestone", 101),
    ("Chiseled Stone", 120),
    ("Engraved Stone", 170),
    ("Moonstone", 553),
    ("Smoothestone", 774),
    ("Burnt Toast", 100),
    ("Shiny Stone", 278),
    ("Twice Baked Potato", 100),
    ("Shiny Rock", 208),
    ("The Lost Night", 404),
    ("Gold Mist", 4096),
    ("Old Man's Stick", 125),
    ("Angel Tears", 777),
    ("Llama Spit", 140),
    ("Yandel Guide Of The Wind", 603),
    ("Adrian's Sweat", 6666),
    ("Goat's Heart", 201),
    ("Essence Of Adrian", 10000),
    ("Smooth Rock", 153),
    ("Maiden Hair", 181),
    ("Broken Branch", 103),
    ("Golden Fleece", 1005),
    ("Maidens Wool", 180),
    ("Mjolnir", 9909),
    ("Kibble And Bits", 164),
    ("Random Food", 444),
    ("Lucky Can", 778),
    ("Baked Bread", 109),
    ("Busted Bifocals", 507),
    ("The Pen Of Writing", 704),
    ("Temporal Tablet", 7055),
    ("Oracle Stone", 6016),
    ("My Soul", 7777),
    ("Beta Worshippers", 808),
    ("Belle Delphine's Gamer Girl Bath Water", 9988),
    ("Box Of Parts", 503),
    ("Elixir", 611),
    ("Sword Parts", 313),
    ("Bone Handle", 215),
    ("Some Random Guy's Spleen", 630),
    ("Gold", 746),
    ("Rubies", 847),
    ("Diamonds", 1021),
    ("Gold Dust", 401),
    ("Ingots", 1053),
    ("Copper", 305),
    ("Iron", 407),
    ("Bronze", 349),
    ("Precious Metal", 939),
    ("Fairy Dust", 991),
    ("Fairy Wings", 998),
    ("Goat", 400),
    ("Magical Water", 221),
    ("Amber Amulet", 4015),
    ("Dragon's Heart", 8888),
    ("Glowing Stone", 1035),
    ("Blood", 122),
    ("Necronomicon", 9612),
    ("Mysterious Tablet", 6014),
    ("Book Of Spells", 6066),
    ("Berhala", 179),
    ("Arcane Stone", 6135),
    ("Statue", 507),
    ("Pixie Dust", 779),
    ("Unicorn Horn", 777),
    ("Iron Ingot", 507),
    ("Hand Guard", 704),
    ("Toilet Paper", 9999)
]


def get_item() -> Dict[str, Union[str, int]]:
    item = secrets.choice(items)
    return {"name": item[0], "value": item[1]}
