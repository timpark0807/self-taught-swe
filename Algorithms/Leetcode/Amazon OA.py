import heapq
import unittest

def amazon_echo(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    """
    Input:
        nc -> integer representing different companies
        topn -> N return the top frequent
        numReviews -> integers
        reviews -> list of string

    Question source: https://leetcode.com/discuss/interview-question/415729/
    """
    # O(clogc) -> where c is the number of competitors
    competitors.sort()
    d = {competitor:0 for competitor in competitors}

    # O(mn) -> where m is number of reviews and n is number of letters per review
    processed_reviews = process_reviews(reviews)

    # O(m) -> m is number of reviews which is number of processed reviews
    for review in processed_reviews:
        for word in review:
            if word in d:
                d[word] += 1
                break
    heap = []
    # O(c) -> c is number of competitors and that is how many items will be in dictionary
    for company, num_reviews in d.items():
        heapq.heappush(heap, (-num_reviews, company))

    answer = []

    # O(K) -> where K is the top competitors we want
    while topNCompetitors > 0:
        answer.append(heapq.heappop(heap)[1])
        topNCompetitors -= 1
        
    # O(clogc + mn + m + c + K)
    # Where...
    # c is number of competitors
    # m is number of reviews
    # n is number of letters per review
    # K is top competitors
    return answer 


def process_reviews(reviews):
    """
    Input -> list of strings
    Output -> List of lists of strings

    Returns reviews in a list of strings, all lowercases
    """
    processed = []
    words = []
    letters = []
    for review in reviews:
        for letter in review:
            if letter.isalpha():
                letters.append(letter.lower())
            elif len(letters) > 0:
                words.append(''.join(letters))
                letters = []
        if len(letters) > 0:
            words.append(''.join(letters))
        processed.append(words)
        words = []

    return processed

class Test(unittest.TestCase):
    def test_solution(self):
        numCompetitors = 6
        topNCompetitors = 2
        competitors = ['newshop', 'shopnow', 'afshion', 'fashionbeats', 'mymarket']
        numReviews = 6
        reviews = ['newshop is  providing services.', 'Thanks Newshop for the quicky delivery.', 'fashionbeats has great service', 'lets go newshop','someething something mymarket']
        answer = amazon_echo(numCompetitors, topNCompetitors, competitors, numReviews, reviews)
        self.assertEqual(answer, ['newshop', 'fashionbeats'])
        
    def test_solution2(self):
        numCompetitors = 6
        topNCompetitors = 2
        competitors = ['newshop', 'shopnow', 'afshion', 'fashionbeats', 'mymarket']
        numReviews = 6
        reviews = ['shopnow is  providing services.', 'Thanks newshop for the quicky delivery.', 'shopnow has great service', 'lets go newshop','someething something mymarket']
        answer = amazon_echo(numCompetitors, topNCompetitors, competitors, numReviews, reviews)
        self.assertEqual(answer, ['newshop', 'shopnow'])


if __name__ == '__main__':
    unittest.main()






