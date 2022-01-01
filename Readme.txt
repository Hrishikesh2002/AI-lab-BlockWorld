Usage:
    python 1.py <input file> <explore type> <heuristic type>

    <input file>
    Path of the input txt file which has format as specified below

    <explore type>
    Option for choosing explore type as below:
    0 - Best First Search
    1 - Hill Climb Approach

    <heuristic type>
    Option for chooseing heuristic as below:
    0 - Manhattan
    1 - Euclidean
    2 - RelPos

Input Format:
    First the start state should be specified, one stack on each line with characters (without spaces in between) corresponding to the blocks listed in order of bottom to top. So, each stack read from bottom to top is the corresponding line in input.txt read from left to right . Post this the goal state should specified after a blank line in a similar format.

    Example:
    EBF
    DA
    C

    ADB
    EFC
    
    
    