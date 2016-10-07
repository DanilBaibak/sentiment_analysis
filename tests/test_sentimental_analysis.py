import unittest
from ..estimator import Estimator


class TestSentimentalAnalysis(unittest.TestCase):
    def setUp(self):
        self.estimator = Estimator()

    def test_general(self):
        estimation_1 = self.estimator.estimate(
            'The staff was nice and helpful, but it was so noisy both late at night outside, ' +
            'and early in the morning with the staff preparing breakfast literally right outside our door ' +
            'that I have to give this a low score. Plus, the rooms felt a little dirty.'
        )
        estimation_2 = self.estimator.estimate(
            'This hotel is situated in a perfect location for walking and sightseeing. ' +
            'However, the rooms were loud and the staff was apathetic and not friendly. ' +
            'In fact the owner was borderline rude and certainly arrogant.'
        )

        self.assertEqual(estimation_1, 0.5)
        self.assertEqual(estimation_2, -3)

    def test_positive(self):
        estimation_1 = self.estimator.estimate(
            'Great location, really pleasant and clean rooms, but the thing that makes this such a good place ' +
            'to stay are the staff. All of the people are incredibly helpful and generous with their time'
        )
        estimation_2 = self.estimator.estimate(
            'The staff is amazing, friendly and helpful and will do anything help make your stay more pleasant. ' +
            'The location, service, rooms are all perfect.'
        )
        estimation_3 = self.estimator.estimate(
            'People at the reception are very kind and our room was big, clean and comfortable'
        )
        estimation_4 = self.estimator.estimate(
            'Quiet, the tastiest breakfast place around the corner, walking distance or very close ' +
            'distance to Empire State, Rockefeller, etc.'
        )
        estimation_5 = self.estimator.estimate(
            'What\'s so wonderful is that very rarely does a good book turn into a movie that is not only good, ' +
            'but if possible better than the novel it was based on.'
        )

        self.assertEqual(estimation_1, 8)
        self.assertEqual(estimation_2, 6)
        self.assertEqual(estimation_3, 4)
        self.assertEqual(estimation_4, 3)
        self.assertEqual(estimation_5, 5)

    def test_negative(self):
        estimation_1 = self.estimator.estimate(
            'The area is not nice(dirty),the building is in bad shape. The stairway going up to the 3rd floor ' +
            'where the rooms are located was so shocking, discouraging & very dirty!!!'
        )
        estimation_2 = self.estimator.estimate(
            'The carpets are dirty and there is no lift although someone will assist you carrying your bags ' +
            'up two flights of stars, then waits in your room awkwardly for a tip.' +
            'Sneered at the euro we gave him. The staff at reception are not welcoming and seem to be unhelpful.'
        )
        estimation_3 = self.estimator.estimate(
            'I was in this hotel to work, the room was terribly noisy, walls are poorly isolated'
        )
        estimation_4 = self.estimator.estimate(
            'This movie is just bad. This movie is poor from beginning to end. Freddy is at his cartoon character worst.'
        )
        estimation_5 = self.estimator.estimate(
            'Writing the required ten lines is incredibly difficult for such a disgraceful piece of cinema. ' +
            'What more can you say than reiterate how truly awful the acting is.'
        )

        self.assertEqual(estimation_1, -7)
        self.assertEqual(estimation_2, -4)
        self.assertEqual(estimation_3, -2)
        self.assertEqual(estimation_4, -3.5)
        self.assertEqual(estimation_5, -3)

# if __name__ == '__main__':
#     unittest.main()
