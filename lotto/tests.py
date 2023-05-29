from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):

    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text = 'selected number')
        g.generate()

        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20) # test 한 건에 대해 결과가 트루여야 통과

# TDD (Test Driven Development)
# 테스트케이스 먼저 써놓고 이를 충족시키는 방향으로 코드를 짬