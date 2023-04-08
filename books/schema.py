import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quizzes, Question, Answer


# class BooksType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class Query(graphene.ObjectType):
#     all_books = graphene.List(BooksType)
#
#     def resolve_all_books(self,  info, **kwargs):
#         return Book.objects.all()
#
#
# schema = graphene.Schema(query=Query)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name']


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ['id', 'title', 'category',]


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ['title', 'quiz']


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text']


class Query(graphene.ObjectType):
    # quiz = graphene.String()
    #
    # @staticmethod
    # def resolve_quiz(root, info):
    #     return f"This is Question"

    # all_quizzes = DjangoListField(QuizzesType)

    # all_quizzes = graphene.List(QuizzesType)
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    # all_questions = graphene.List(QuestionType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    @staticmethod
    def resolve_all_quizzes(root, info, id):
        # return Quizzes.objects.all()
        # return Quizzes.objects.filter(id=1)
        return Quizzes.objects.get(pk=id)

    @staticmethod
    def resolve_all_questions(root, info, id):
        # return Question.objects.all()
        return Question.objects.get(pk=id)

    @staticmethod
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


class AddCategoryMutation(graphene.Mutation):
    """Add New Category"""
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return AddCategoryMutation(category=category)


class UpdateCategoryMutation(graphene.Mutation):
    """Update Category"""
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategoryMutation(category=category)


class DeleteCategoryMutation(graphene.Mutation):
    """Update Category"""
    class Arguments:
        id = graphene.ID()
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info,  id):
        category = Category.objects.get(id=id)
        category.delete()
        return ""


class Mutation(graphene.ObjectType):
    add_category = AddCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
