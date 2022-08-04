from django.test import TestCase

from .models import *





class TestModelBrand(TestCase):
    def setUp(self):
        Brand.objects.create(name='Shivaki')
        Brand.objects.create(name='Samsung')
        return super().setUp()

    def test_count_regions(self):
        self.assertEqual(Brand.objects.all().count(), 2)

    def test_real_object(self): 
        self.assertEqual(Brand.objects.get(
            name='Shivaki').name, 'Shivaki')
        self.assertEqual(Brand.objects.get(
            name='Samsung').name, 'Samsung')


class TestModelSize(TestCase):
    def setUp(self):
        Size.objects.create(Size='katta')
        Size.objects.create(Size='kichkina')
        return super().setUp()

    def test_count_Size(self):
        self.assertEqual(Size.objects.all().count(), 2)

    def test_real_object(self): 
        self.assertEqual(Size.objects.get(
            Size='katta').Size, 'katta')
        self.assertEqual(Size.objects.get(
            Size='kichkina').Size, 'kichkina')



# class TestModelColor(TestCase):
#     def setUp(self):
#         Color.objects.create(name='qora')
#         Color.objects.create(name='oq')
#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Color.objects.all().count(), 2)

#     def test_real_object(self): 
#         self.assertEqual(Color.objects.get(
#             name='qora').Color, 'qora')
#         self.assertEqual(Brand.objects.get(
#             name='oq').Color, 'oq')



# class TestModelCountry(TestCase):
#     def setUp(self):
#         Country.objects.create(Country='uzb')
#         Country.objects.create(Country='ru')
#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Country.objects.all().count(), 2)

#     def test_real_object(self): 
#         self.assertEqual(Country.objects.get(
#             Country='uzb').Country, 'uzb')
#         self.assertEqual(Country.objects.get(
#             Country='ru').Country, 'ru')




# class TestModelCondition(TestCase):
#     def setUp(self) -> None:
#         Condition.objects.create(Condition="rus")
#         Condition.objects.create(Condition="uzb")
#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Condition.objects.all().count(), 2)

#     def test_real_object(self):
#         self.assertEqual(Condition.objects.get(
#             name="uzb").Condition, "uzb")
#         self.assertEqual(Condition.objects.get(
#             name='uzb').Condition, "uzb")


# class TestModelRegion(TestCase):
#     def setUp(self) -> None:
#         country = Country.objects.create(name="uzbekistan")
#         country1 = Country.objects.create(name="uzbekistan2")
#         Region.objects.create(name="tashkent", country=country)
#         Region.objects.create(name="tashkent", country=country1)
#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Region.objects.all().count(), 2)


# class TestModelCompany(TestCase):
#     def setUp(self) -> None:
#         country = Country.objects.create(name="uzbekistan")
#         country1 = Country.objects.create(name="uzbekistan2")
#         region = Region.objects.create(name="tashkent", country=country)
#         region1 = Region.objects.create(name="tashkent", country=country1)
#         Company.objects.create(name="sss", region=region)
#         Company.objects.create(name="sss", region=region1)
#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Region.objects.all().count(), 2)


# class TestModelBrend(TestCase):
#     def setUp(self) -> None:
#         country = Country.objects.create(name="uzbekistan")
#         country1 = Country.objects.create(name="uzbekistan2")
#         region = Region.objects.create(name="tashkent", country=country)
#         region1 = Region.objects.create(name="tashkent", country=country1)
#         companiy = Company.objects.create(name="sss", region=region)
#         companiy1 = Company.objects.create(name="sss", region=region1)
#         Brend.objects.create(name="sss", companiy_id=companiy)
#         Brend.objects.create(name="sss", companiy_id=companiy1)

#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Brend.objects.all().count(), 2)


# class TestModelGender(TestCase):
#     def setUp(self) -> None:
#         Gender.objects.create(gender="woman")
#         Gender.objects.create(gender="male")

#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Gender.objects.all().count(), 2)


# class TestModelCategoryType(TestCase):
#     def setUp(self) -> None:
#         Category_type.objects.create(type="qattiq")
#         Category_type.objects.create(type="yumshoq")

#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Category_type.objects.all().count(), 2)


# class TestModelDelivery(TestCase):
#     def setUp(self) -> None:
#         Delivery.objects.create(delivery="True")
#         Delivery.objects.create(delivery="False")

#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Delivery.objects.all().count(), 2)


# class TestModelToys(TestCase):
#     def setUp(self) -> None:
#         category = Category.objects.create(from_category=0, to_category=10)
#         category1 = Category.objects.create(from_category=10, to_category=15)
#         country = Country.objects.create(name="uzbekistan")
#         country1 = Country.objects.create(name="uzbekistan2")
#         region = Region.objects.create(name="tashkent", country=country)
#         region1 = Region.objects.create(name="tashkent", country=country1)
#         companiy = Company.objects.create(name="sss", region=region)
#         companiy1 = Company.objects.create(name="sss", region=region1)
#         brend = Brend.objects.create(name="sss", companiy_id=companiy)
#         brend2 = Brend.objects.create(name="sss", companiy_id=companiy1)
#         gender = Gender.objects.create(gender="woman")
#         gender2 = Gender.objects.create(gender="male")
#         toys_type = Category_type.objects.create(type="qattiq")
#         toys_type2 = Category_type.objects.create(type="yumshoq")
#         delivery = Delivery.objects.create(delivery="True")
#         delivery2 = Delivery.objects.create(delivery="False")
#         Toys.objects.create(name="tedy", price=100, category=category, brend=brend,
#                             gender=gender, toys_type=toys_type, img="static/images/1.jpg", delivery=delivery)
#         Toys.objects.create(name="barby", price=100, category=category1, brend=brend2,
#                             gender=gender2, toys_type=toys_type2, img="static/images/1.jpg", delivery=delivery2)

#         return super().setUp()

#     def test_count_regions(self):
#         self.assertEqual(Toys.objects.all().count(), 2)


# class TestModelOrder(TestCase):
#     def setUp(self) -> None:
#         user = User.objects.create(last_name="samandar", first_name="boriyev",
#                                    username="samandar01", email="samandar@gmail.com", img="static/images/1.jpg")
#         category = Category.objects.create(from_category=0, to_category=10)
#         category1 = Category.objects.create(from_category=10, to_category=15)
#         country = Country.objects.create(name="uzbekistan")
#         country1 = Country.objects.create(name="uzbekistan2")
#         region = Region.objects.create(name="tashkent", country=country)
#         region1 = Region.objects.create(name="tashkent", country=country1)
#         companiy = Company.objects.create(name="sss", region=region)
#         companiy1 = Company.objects.create(name="sss", region=region1)
#         brend = Brend.objects.create(name="sss", companiy_id=companiy)
#         brend2 = Brend.objects.create(name="sss", companiy_id=companiy1)
#         gender = Gender.objects.create(gender="woman")
#         gender2 = Gender.objects.create(gender="male")
#         toys_type = Category_type.objects.create(type="qattiq")
#         toys_type2 = Category_type.objects.create(type="yumshoq")
#         delivery = Delivery.objects.create(delivery="True")
#         delivery2 = Delivery.objects.create(delivery="False")
#         toys = Toys.objects.create(name="tedy", price=100, category=category, brend=brend,
#                                    gender=gender, toys_type=toys_type, img="static/images/1.jpg", delivery=delivery)
#         toys2 = Toys.objects.create(name="barby", price=100, category=category1, brend=brend2,
#                                     gender=gender2, toys_type=toys_type2, img="static/images/1.jpg", delivery=delivery2)
#         Order.objects.create(user=user, toys=toys)
#         Order.objects.create(user=user, toys=toys)
#         return super().setUp()

#     def test_count_order(self):
#         self.assertEqual(Order.objects.all().count(), 2)


# class TestAuhtorViews(TestCase):

#     def setUp(self) -> None:
#         self.c = Client()
#         self.response_post = self.c.post(
#             '/category/add', {'from_category': 0, 'to_category': 10})
#         self.response_get = self.c.get('/category/')
#         return super().setUp()

#     def test_create_author(self):
#         self.assertEqual(self.response_post.status_code, 302)