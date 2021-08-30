from enum import Enum

NUM_ATTRIBUTES = 14 + 1
print(f"Using the {NUM_ATTRIBUTES-1} most frequent attributes.")


class Attribute(Enum):
    other = 0
    price = 1
    availableSizes = 2
    customerRating = 3
    brand = 4
    info = 5
    color = 6
    embellishment = 7
    pattern = 8
    hemLength = 9
    skirtStyle = 10
    dressStyle = 11
    material = 12
    clothingStyle = 13
    necklineStyle = 14
    size = 15
    jacketStyle = 16
    sweaterStyle = 17
    hemStyle = 18
    sleeveStyle = 19
    waistStyle = 20
    sleeveLength = 21
    clothingCategory = 22
    skirtLength = 23
    soldBy = 24
    madeIn = 25
    ageRange = 26
    waterResistance = 27
    warmthRating = 28
    sequential = 29
    hasPart = 30
    forOccasion = 31
    forGender = 32
    amountInStock = 33

    @classmethod
    def length(cls):
        return NUM_ATTRIBUTES

    @classmethod
    def from_str(cls, attribute):
        value = 0
        if attribute == "price":
            value = cls.price.value
        elif attribute == "availableSizes":
            value = cls.availableSizes.value
        elif attribute == "customerRating":
            value = cls.customerRating.value
        elif attribute == "brand":
            value = cls.brand.value
        elif attribute == "info":
            value = cls.info.value
        elif attribute == "color":
            value = cls.color.value
        elif attribute == "embellishment":
            value = cls.embellishment.value
        elif attribute == "pattern":
            value = cls.pattern.value
        elif attribute == "hemLength":
            value = cls.hemLength.value
        elif attribute == "skirtStyle":
            value = cls.skirtStyle.value
        elif attribute == "dressStyle":
            value = cls.dressStyle.value
        elif attribute == "material":
            value = cls.material.value
        elif attribute == "clothingStyle":
            value = cls.clothingStyle.value
        elif attribute == "necklineStyle":
            value = cls.necklineStyle.value
        elif attribute == "size":
            value = cls.size.value
        elif attribute == "jacketStyle":
            value = cls.jacketStyle.value
        elif attribute == "sweaterStyle":
            value = cls.sweaterStyle.value
        elif attribute == "hemStyle":
            value = cls.hemStyle.value
        elif attribute == "sleeveStyle":
            value = cls.sleeveStyle.value
        elif attribute == "waistStyle":
            value = cls.waistStyle.value
        elif attribute == "sleeveLength":
            value = cls.sleeveLength.value
        elif attribute == "clothingCategory":
            value = cls.clothingCategory.value
        elif attribute == "skirtLength":
            value = cls.skirtLength.value
        elif attribute == "soldBy":
            value = cls.soldBy.value
        elif attribute == "madeIn":
            value = cls.madeIn.value
        elif attribute == "ageRange":
            value = cls.ageRange.value
        elif attribute == "waterResistance":
            value = cls.waterResistance.value
        elif attribute == "warmthRating":
            value = cls.warmthRating.value
        elif attribute == "sequential":
            value = cls.sequential.value
        elif attribute == "hasPart":
            value = cls.hasPart.value
        elif attribute == "forOccasion":
            value = cls.forOccasion.value
        elif attribute == "forGender":
            value = cls.forGender.value
        elif attribute == "amountInStock":
            value = cls.amountInStock.value
        if value < NUM_ATTRIBUTES:
            return value
        else:
            return cls.other.value

    @classmethod
    def from_number(cls, value):
        if value == cls.price.value:
            return "price"
        elif value == cls.availableSizes.value:
            return "availableSizes"
        elif value == cls.customerRating.value:
            return "customerRating"
        elif value == cls.brand.value:
            return "brand"
        elif value == cls.info.value:
            return "info"
        elif value == cls.color.value:
            return "color"
        elif value == cls.embellishment.value:
            return "embellishment"
        elif value == cls.pattern.value:
            return "pattern"
        elif value == cls.hemLength.value:
            return "hemLength"
        elif value == cls.skirtStyle.value:
            return "skirtStyle"
        elif value == cls.dressStyle.value:
            return "dressStyle"
        elif value == cls.material.value:
            return "material"
        elif value == cls.clothingStyle.value:
            return "clothingStyle"
        elif value == cls.necklineStyle.value:
            return "necklineStyle"
        elif value == cls.size.value:
            return "size"
        elif value == cls.jacketStyle.value:
            return "jacketStyle"
        elif value == cls.sweaterStyle.value:
            return "sweaterStyle"
        elif value == cls.hemStyle.value:
            return "hemStyle"
        elif value == cls.sleeveStyle.value:
            return "sleeveStyle"
        elif value == cls.waistStyle.value:
            return "waistStyle"
        elif value == cls.sleeveLength.value:
            return "sleeveLength"
        elif value == cls.clothingCategory.value:
            return "clothingCategory"
        elif value == cls.skirtLength.value:
            return "skirtLength"
        elif value == cls.soldBy.value:
            return "soldBy"
        elif value == cls.madeIn.value:
            return "madeIn"
        elif value == cls.ageRange.value:
            return "ageRange"
        elif value == cls.waterResistance.value:
            return "waterResistance"
        elif value == cls.warmthRating.value:
            return "warmthRating"
        elif value == cls.sequential.value:
            return "sequential"
        elif value == cls.hasPart.value:
            return "hasPart"
        elif value == cls.forOccasion.value:
            return "forOccasion"
        elif value == cls.forGender.value:
            return "forGender"
        elif value == cls.amountInStock.value:
            return "amountInStock"
        else:
            return "other"
