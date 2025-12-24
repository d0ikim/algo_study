#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<int> stage_user_vector(int N, vector<int> stages);
vector<float> get_failure_rates(vector<int> users, int users_count, int N);
vector<int> get_stages_failure_rate(vector<float> failure_rate, int N);

vector<int> solution(int N, vector<int> stages) {
    vector<int> users = stage_user_vector(N, stages);
    vector<float> failure_rates = get_failure_rates(users, stages.size(), N);
    vector<int> answer = get_stages_failure_rate(failure_rates, N);
    
    return answer;
}

vector<int> stage_user_vector(int N, vector<int> stages)
{
    vector<int> users(1, -1);
    int user_count = stages.size();
    
    for(int i = 1; i <= N; i ++)
    {
        int count = 0;
        for(int j = 0; j < user_count; j ++)
        {
            if (stages.at(j) == i)
            {
                count++;
            }
        }
        
        users.push_back(count);
    }
    
    return users;
}

vector<float> get_failure_rates(vector<int> users, int users_count, int N)
{
    vector<float> failures(1, -1);
    
    for(int i = 1; i <= N; i ++)
    {
        float rate = 0;
        if (users_count > 0)
        {
            int user_stage = users.at(i);
            rate = (float)user_stage / users_count;
            users_count -= user_stage;
        }
        failures.push_back(rate);
    }
    
    return failures;
}

vector<int> get_stages_failure_rate(vector<float> failure_rate, int N)
{
    vector<int> stages;
    
    for(int i = 1; i <= N; i ++)
    {
        float max = failure_rate.at(0);
        int index = 0;
        
        for(int j = 1; j <= N; j ++)
        {
            float rate = failure_rate.at(j);
            if (rate > max)
            {
                max = rate;
                index = j;
            }
        }
        
        failure_rate.at(index) = -1;
        stages.push_back(index);
    }
    
    return stages;
}