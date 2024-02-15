import pandas as pd
import os
from datetime import datetime

x=1
for i in range(10):
    SAMPLE_RATE = 64
    HEADER_LINES = 2

    PARTICIPANTE = x

    ATIVIDADE = 'QD'
    MARCHA = 'G'
    SEQUENCIA = 10
    SENSOR = 'BVP'

    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv')
    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'bvp'})
    init_time_measure = data.iloc[0,0]
    print(data)
    print(init_time_measure)

    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    print(tags)
    print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    print(lines_to_cut_init)

    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES+1
    print(lines_to_cut_end)

    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]
    print(formatted_data.shape)
    formatted_data.plot()

    #reduce sampling from 64 to 32
    formatted_data = formatted_data[0:-1:2]
    print(formatted_data.shape)
    formatted_data.plot()

    print(formatted_data.shape)

    print(formatted_data)

    dataLifeSenior = pd.read_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv',index_col=False)
                                
    diff_rows = formatted_data.shape[0]-dataLifeSenior.shape[0]

    if(diff_rows == 1):
        #remove last row
        formatted_data = formatted_data[:-1] 

    dataLifeSenior["bvp"] = formatted_data.values
    print(dataLifeSenior)


    #export the file to specific activity
    dataLifeSenior.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1

x=1
for i in range(10):
    SAMPLE_RATE = 64
    HEADER_LINES = 2

    PARTICIPANTE = x

    ATIVIDADE = 'QD'
    MARCHA = 'G'
    SEQUENCIA = 11
    SENSOR = 'BVP'

    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv')
    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'bvp'})
    init_time_measure = data.iloc[0,0]
    print(data)
    print(init_time_measure)

    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    print(tags)
    print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    print(lines_to_cut_init)

    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES+1
    print(lines_to_cut_end)

    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]
    print(formatted_data.shape)
    formatted_data.plot()

    #reduce sampling from 64 to 32
    formatted_data = formatted_data[0:-1:2]
    print(formatted_data.shape)
    formatted_data.plot()

    print(formatted_data.shape)

    print(formatted_data)

    dataLifeSenior = pd.read_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv',index_col=False)
                                
    diff_rows = formatted_data.shape[0]-dataLifeSenior.shape[0]

    if(diff_rows == 1):
        #remove last row
        formatted_data = formatted_data[:-1] 

    dataLifeSenior["bvp"] = formatted_data.values
    print(dataLifeSenior)


    #export the file to specific activity
    dataLifeSenior.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1


x=1
for i in range(10):
    SAMPLE_RATE = 64
    HEADER_LINES = 2

    PARTICIPANTE = x

    ATIVIDADE = 'QD'
    MARCHA = 'G'
    SEQUENCIA = 12
    SENSOR = 'BVP'

    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv')
    print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'bvp'})
    init_time_measure = data.iloc[0,0]
    print(data)
    print(init_time_measure)

    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    print(tags)
    print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    print(lines_to_cut_init)

    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES+1
    print(lines_to_cut_end)

    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]
    print(formatted_data.shape)
    formatted_data.plot()

    #reduce sampling from 64 to 32
    formatted_data = formatted_data[0:-1:2]
    print(formatted_data.shape)
    formatted_data.plot()

    print(formatted_data.shape)

    print(formatted_data)

    dataLifeSenior = pd.read_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv',index_col=False)
                                
    diff_rows = formatted_data.shape[0]-dataLifeSenior.shape[0]

    if(diff_rows == 1):
        #remove last row
        formatted_data = formatted_data[:-1] 

    dataLifeSenior["bvp"] = formatted_data.values
    print(dataLifeSenior)


    #export the file to specific activity
    dataLifeSenior.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1

