from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-01-01')
        self.assertEqual(str(activity), 'Test User - Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Test User - 100')
