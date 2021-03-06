from mongoengine import Document, fields


class Card(Document):
    # define every field
    cardId = fields.StringField()
    dbfId = fields.StringField()
    name = fields.StringField()
    cardSet = fields.StringField()
    type = fields.StringField()
    locale = fields.StringField()
    playerClass = fields.StringField()
    img = fields.StringField()
    imgGold = fields.StringField()
    text = fields.StringField()
    health = fields.IntField()
    artist = fields.StringField()
    mechanics = fields.DynamicField()
    faction = fields.StringField()
    cost = fields.IntField()
    attack = fields.IntField()
    durability = fields.IntField()
    rarity = fields.StringField()
    flavor = fields.StringField()
    collectible = fields.BooleanField()
    race = fields.StringField()
    elite = fields.BooleanField()
    armor = fields.StringField()
