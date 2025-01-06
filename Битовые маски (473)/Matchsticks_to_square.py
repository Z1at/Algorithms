"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick,
but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

>>> makesquare([1,1,2,2,2])
True

>>> makesquare([3,3,4,4,4])
False
"""


from typing import List


def makesquare(nums: List[int]) -> bool:
    # If there are no matchsticks, then we can't form any square.
    if not nums:
        return False

    # Number of matchsticks
    L = len(nums)

    # Possible perimeter of our square
    perimeter = sum(nums)

    # Possible side of our square from the given matchsticks
    possible_side =  perimeter // 4

    # If the perimeter isn't equally divisible among 4 sides, return False.
    if possible_side * 4 != perimeter:
        return False

    # Memoization cache for the dynamic programming solution.
    memo = {}

    # mask and the sides_done define the state of our recursion.
    def recurse(mask, sides_done):

        # This will calculate the total sum of matchsticks used till now using the bits of the mask.
        total = 0
        for i in range(L - 1, -1, -1):
            if not (mask & (1 << i)):
                total += nums[L - 1 - i]

        # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
        if total > 0 and total % possible_side == 0:
            sides_done += 1

        # If we were successfully able to form 3 sides, return True
        if sides_done == 3:
            return True

        # If this recursion state has already been calculated, just return the stored value.
        if (mask, sides_done) in memo:
            return memo[(mask, sides_done)]

        # Common variable to store answer from all possible further recursions from this step.
        ans = False

        # rem stores available space in the current side (incomplete).
        c = int(total / possible_side)
        rem = possible_side * (c + 1) - total

        # Iterate over all the matchsticks
        for i in range(L - 1, -1, -1):

            # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
            if nums[L - 1 - i] <= rem and mask&(1 << i):

                # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                if recurse(mask ^ (1 << i), sides_done):
                    ans = True
                    break
        # cache the result for the current recursion state.
        memo[(mask, sides_done)] = ans
        return ans

    # recurse with the initial mask with all matchsticks available.
    return recurse((1 << L) - 1, 0)


"""
Задача является np-полной и не получится её решить быстро
Самое базовое решение:
Три раза решить задачу о нахождении чисел в массиве, сумма которых равна заданному
target задаём как sum(nums) / 4 и если три раза получается решить эту задачу, то значит true, иначе false
При этом, после каждого решения нужно запоминать какие числа уже использовали
Почему три? Потому что, если мы можем сформировать три стороны, то оставшиеся числа автоматически сформируют четвёртую


Если нужно более лучшее решение, то вот оно:
In any dynamic programming problem, what's important is that our problem must be breakable into smaller subproblems and 
also, these subproblems show some sort of overlap which we can save upon by caching or memoization.

Suppose we have 3,3,4,4,5,5 as our matchsticks that have been used already to construct some of the sides of our square 
(Note: not all the sides may be completely constructed at all times.)

If the square side is 8, then there are many possibilities for how the sides can be constructed using the matchsticks 
above. We can have
  (4, 4), (3, 5), (3, 5) -----------> 3 sides fully constructed.
  (3, 4), (3, 5), (4), (5) ---------> 0 sides completely constructed.
  (3, 3), (4, 4), (5), (5) ---------> 1 side completely constructed.
  
As we can see above, there are multiple ways to use the same set of matchsticks and land up in completely different 
recursion states.

This means that if we just keep track of what all matchsticks have been used and which all are remaining, it won't 
properly define the state of recursion we are in or what subproblem we are solving.

A single set of used matchsticks can represent multiple different unrelated subproblems and that is just not right.

We also need to keep track of number of sides of the square that have been completely formed till now.

Also, an important thing to note in the example we just considered was that if the matchsticks being used are 
[3,3,4,4,5,5] and the side of the square is 8, then we will always consider that arrangement that forms the most number 
of complete sides over that arrangement that leads to incomplete sides. Hence, the optimal arrangement here is 
(4,4),(3,5),(3,5) with 3 complete sides of the square.

We know that the overall sum of these matchsticks can be split equally into 4 halves. The only thing we don't know is 
if 4 equal halves can be carved out of the given set of matchsticks. For that also we need to keep track of the number 
of sides completely formed at any point in time. If we end up forming 4 equal sides successfully then naturally we would 
have used up all of the matchsticks each being used exactly once and we would have formed a square.





It is very clear from the pseudo-code above that the state of a recursion is defined by two variables matchsticks_used 
and sides_formed. Hence, these are the two variables that will be used to memoize or cache the results for that 
specific subproblem.

The question however is how do we actually store all the matchsticks that have been used? We want a memory efficient 
solution for this.

If we look at the question's constraints, we find that the max number of matchsticks we can have are 15. That's a pretty 
small number and we can make use of this constraint.

All we need to store is which of the matchsticks from the original list have been used. We can use a Bit-Map for this

We will use N number of bits, one for each of the matchsticks (N is at max 15 according to the question's constraints). 
Initially we will start with a bit mask of all 1s and then as we keep on using the matchsticks, we will keep on setting 
their corresponding bits to 0.

Another implementation trick that helps optimize this solution is that we don't really need to see if 4 sides have 
been completely formed.

This is because, we already know that the sum of all the matchsticks is divisible by 4. So, if 3 equal sides have been 
formed by using some of the matchsticks, then the remaining matchsticks would definitely form the remaining side of 
our square.

Hence, we only need to check if 3 sides of our square can be formed or not.
"""