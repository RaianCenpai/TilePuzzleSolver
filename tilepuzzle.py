# Homework Assignment 1 - tilepuzzle
# Ryan Cen

import copy

# The maximum recursion depth for one path from start to goal.
MAX_RECURSION_DEPTH = 10

def tilepuzzle(start,goal):
    return reverse(statesearch([start],goal,[]))

def statesearch(unexplored,goal,path):
    if unexplored == [] or len(path) > MAX_RECURSION_DEPTH:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:       
        result = statesearch(generateNewStates(head(unexplored), path), goal, cons(head(unexplored), path))
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored), goal, path)

def reverseEach(listOfLists):
    result = []
    for st in listOfLists:
        result.append(reverse(st))
    return result

def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst

# Finds the location of the zero and then generates new states for each direction that it
# can possible go and only appends it to the list of newStates if the state does not
# already exist in the path.
def generateNewStates(currState, path):
    newStates = []
    for i in range(len(currState)):
        if 0 in currState[i]:
            subIndex = currState[i].index(0)
            index = i
    
    if index + 1 != 1:
        newUpState = generateNewUpState(currState, index, subIndex)
        if(newUpState not in path):
            newStates.append(newUpState)

    if index + 1 != len(currState):
        newDownState = generateNewDownState(currState, index, subIndex)
        if(newDownState not in path):
            newStates.append(newDownState)

    if subIndex + 1 != 1:
        newLeftState = generateNewLeftState(currState, index, subIndex)
        if(newLeftState not in path):
            newStates.append(newLeftState)

    if subIndex + 1 != len(currState[1]):
        newRightState = generateNewRightState(currState, index, subIndex)
        if(newRightState not in path):
            newStates.append(newRightState)

    return newStates

# List of functions that generate a new state given the location of the zero as index and
# subindex and the current state as currState. It swaps the location of the zero to which 
# ever direction specified in the function name and returns the new state.
def generateNewUpState(currState, index, subIndex):
    newUpState = copy.deepcopy(currState)
    newUpState[index][subIndex], newUpState[index-1][subIndex] = newUpState[index-1][subIndex], newUpState[index][subIndex]
    return newUpState

def generateNewDownState(currState, index, subIndex):
    newDownState = copy.deepcopy(currState)
    newDownState[index][subIndex], newDownState[index+1][subIndex] = newDownState[index+1][subIndex], newDownState[index][subIndex]
    return newDownState

def generateNewLeftState(currState, index, subIndex):
    newLeftState = copy.deepcopy(currState)
    newLeftState[index][subIndex], newLeftState[index][subIndex-1] = newLeftState[index][subIndex-1], newLeftState[index][subIndex]
    return newLeftState

def generateNewRightState(currState, index, subIndex):
    newRightState = copy.deepcopy(currState)
    newRightState[index][subIndex], newRightState[index][subIndex+1] = newRightState[index][subIndex+1], newRightState[index][subIndex]
    return newRightState
