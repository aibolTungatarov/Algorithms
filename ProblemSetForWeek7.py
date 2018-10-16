{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##First Task\n",
    "def pow3(x, n):\n",
    "    r = 1\n",
    "    while n:\n",
    "        if n % 2 == 1:\n",
    "            r *= x\n",
    "            n -= 1\n",
    "        x *= x\n",
    "        n /= 2\n",
    "    return r\n",
    "\n",
    "## Second Task\n",
    "def loc_peaks(arr,i,j):\n",
    "    middle = math.floor(((i+j)/2))\n",
    "    if (arr[middle] > arr[middle-1] and arr[middle] > arr[middle+1]): \n",
    "        return arr[middle]\n",
    "    elif arr[middle] < arr[middle-1]:\n",
    "        return loc_peaks(arr,i,middle-1)\n",
    "    elif arr[middle] < arr[middle+1]:\n",
    "        return loc_peaks(arr,middle+1,j)\n",
    "    \n",
    "    \n",
    "    \n",
    "## Third Task    \n",
    "def findMin(arr):\n",
    "    minNum = 100000000\n",
    "    minNumIndex = 0\n",
    "    for i in range(len(arr)):\n",
    "        if minNum > arr[i]:\n",
    "            minNum = arr[i]\n",
    "            minNumIndex = i\n",
    "    return minNum,minNumIndex\n",
    "def findShiftK(arr):\n",
    "    minNum = findMin(arr)[0]\n",
    "    return minNumIndex = findMin(arr)[1]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
