'''Exercise 2

AGENT SELECTOR'''


import random

'''Function takes input on agent and their data 
Dictionary of agent for data set.
List of agent details in each agent
1st element will be agent is available or not- yes or no 
2nd element will be time from agent is available
3rd element will have role of agent'''

def agent_input():
    n=int(input("No. of agent: "))
    dict_agent={}
    for i in range(n):
        list=[]
        print("\n\nAgent "+str(i+1)+" Details:")
        available=input("Is agent available or not (yes or no): ")
        list.append(available)
        if(available=='yes'):
            time=input("Time since agent is available in hrs: ")
            list.append(time)
        role=input("Enter role of a agent: ").lower()
        list.append(role)
        dict_agent[i+1]=list
    return(dict_agent)    

  

'''Issue fit to which role , we will obtain list of agent
   who match with the issue role'''

def return_agent(agent,agent_selection_mode,Issue_role):
    agent_fit_role=[]
    agent_available=[]
    
    for i in agent:
        if(agent[i][0]=='yes'):
            agent_available.append(i)
    
    for i in agent_available:
        if(Issue_role==agent[i][2]):
            agent_fit_role.append(i) 
    
    
    '''To present issue to one or more agent'''  
      

    if(agent_selection_mode=='All available'):
        return(agent_fit_role)
    
    elif(agent_selection_mode=='Least Busy'):
        time_max=0
        for i in agent_fit_role:
            if(int(agent[i][1])>time_max):
                time_max=int(agent[i][1])
                agent_issue=i
        return(agent_issue)     
    
    elif(agent_selection_mode=='Random'):
        agent_issue=random.choice(agent_fit_role)
        return(agent_issue)
         

agent=agent_input()
print("\n\n",agent)

agent_selection_mode=input('Enter- All available" or "Least Busy" or "Random":  ')

Issue_role=input("Role to which issue belongs:  ").lower() 

available_agent=return_agent(agent,agent_selection_mode,Issue_role)
     
print("Issue presented to: Agent",available_agent)     


'''Test Cases 1'''
agent={1: ['yes', '23', 'sales'], 2: ['no ', 'sales'], 3: ['yes', '24', 'sales'],\
       4: ['yes', '16', 'speaker'], 5: ['no', 'sales'], 6: ['yes', '16', 'sales']}
available_agent=return_agent(agent,"Least Busy","sales")    
print('PASS' if(3==available_agent) else "FAIL")   
        
'''Test Cases 2'''
agent={1: ['yes', '23', 'sales'], 2: ['no ', 'sales'], 3: ['yes', '24', 'sales'],\
       4: ['yes', '16', 'speaker'], 5: ['no', 'sales'], 6: ['yes', '16', 'sales']}
available_agent=return_agent(agent,"All available","sales")    
print('PASS' if([1,3,6]==available_agent) else "FAIL") 

'''Test Cases 3'''
agent={1: ['yes', '23', 'sales'], 2: ['no ', 'sales'], 3: ['yes', '24', 'sales'],\
       4: ['yes', '16', 'speaker'], 5: ['no', 'sales'], 6: ['yes', '16', 'sales']}
available_agent=return_agent(agent,"Random","sales")    
print('PASS' if(1==available_agent or 3==available_agent or 6==available_agent) else "FAIL")           
        
    
 
   





    