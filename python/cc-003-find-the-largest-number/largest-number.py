{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "count=0\n",
    "array=[]\n",
    "while count < 5:\n",
    "  number= int(input('Please enter the number: '))\n",
    "  array.append(number)\n",
    "  count = count +1\n",
    "def findLargestNum(nums):\n",
    "  largest = nums[0]\n",
    "  for i in nums:\n",
    "    if i > largest:\n",
    "      largest = i\n",
    "  return largest\n",
    "print(findLargestNum(array))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "d679073fc1bfd208dd16f6a4b9b77c86332bc8c804a700fb971f0b1411f0c378"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
