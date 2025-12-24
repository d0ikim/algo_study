#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    
    int row = arr1.size();
    int col = arr2.at(0).size();
    int dot_count = arr1.at(0).size();
    
    vector<vector<int>> matrix;
    
    for(int i = 0; i < row; i ++)
    {
        matrix.push_back(vector<int>());
        for (int j = 0; j < col; j ++)
        {
            int number = 0;
            for(int k = 0; k < dot_count; k ++)
            {
                number += arr1.at(i).at(k) * arr2.at(k).at(j);
            }
            
            matrix.at(i).push_back(number);
        }
    }
    
    return matrix;
}