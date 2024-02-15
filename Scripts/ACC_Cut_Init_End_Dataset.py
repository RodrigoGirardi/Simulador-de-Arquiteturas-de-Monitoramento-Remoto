import pandas as pd
import os
from datetime import datetime

x=1
for i in range(10):
    SAMPLE_RATE = 32

    PARTICIPANTE = x

    ATIVIDADE = 'QD'
    MARCHA = 'G'
    SEQUENCIA = 12
    SENSOR = 'ACC'

    HEADER_LINES = 2

    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv') 
    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    #print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})
    init_time_measure = data.iloc[0,0]
    #print(data)

    #print(init_time_measure)


    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    #print(tags)
    #print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    #print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    #print(lines_to_cut_init)
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_init)


    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    #print(lines_to_cut_end)
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_end)


    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]

    #transform to real values according to Empatica Calc
    formatted_data = (formatted_data.values*2)/128

    #print(formatted_data)

    newdata = pd.DataFrame(formatted_data)
    newdata = newdata.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})


    #print(newdata.shape)
    #print(newdata)

    newdata.plot()


    #export the file to specific activity
    newdata.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1


x=1
for i in range(10):
    SAMPLE_RATE = 32

    PARTICIPANTE = x

    ATIVIDADE = 'AVD'
    MARCHA = 'G'
    SEQUENCIA = 2
    SENSOR = 'ACC'

    HEADER_LINES = 2

    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv') 
    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    #print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})
    init_time_measure = data.iloc[0,0]
    #print(data)

    #print(init_time_measure)


    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    #print(tags)
    #print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    #print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    #print(lines_to_cut_init)
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_init)


    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    #print(lines_to_cut_end)
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_end)


    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]

    #transform to real values according to Empatica Calc
    formatted_data = (formatted_data.values*2)/128

    #print(formatted_data)

    newdata = pd.DataFrame(formatted_data)
    newdata = newdata.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})


    #print(newdata.shape)
    #print(newdata)

    newdata.plot()


    #export the file to specific activity
    newdata.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1

x=1
for i in range(10):
    SAMPLE_RATE = 32

    PARTICIPANTE = x

    ATIVIDADE = 'AVD'
    MARCHA = 'G'
    SEQUENCIA = 3
    SENSOR = 'ACC'

    HEADER_LINES = 2

    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv') 
    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    #print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})
    init_time_measure = data.iloc[0,0]
    #print(data)

    #print(init_time_measure)


    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    #print(tags)
    #print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    #print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    #print(lines_to_cut_init)
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_init)


    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    #print(lines_to_cut_end)
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_end)


    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]

    #transform to real values according to Empatica Calc
    formatted_data = (formatted_data.values*2)/128

    #print(formatted_data)

    newdata = pd.DataFrame(formatted_data)
    newdata = newdata.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})


    #print(newdata.shape)
    #print(newdata)

    newdata.plot()


    #export the file to specific activity
    newdata.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1

x=1
for i in range(10):
    SAMPLE_RATE = 32

    PARTICIPANTE = x

    ATIVIDADE = 'AVD'
    MARCHA = 'G'
    SEQUENCIA = 4
    SENSOR = 'ACC'

    HEADER_LINES = 2

    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv') 
    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    #print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})
    init_time_measure = data.iloc[0,0]
    #print(data)

    #print(init_time_measure)


    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    #print(tags)
    #print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    #print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    #print(lines_to_cut_init)
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_init)


    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    #print(lines_to_cut_end)
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_end)


    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]

    #transform to real values according to Empatica Calc
    formatted_data = (formatted_data.values*2)/128

    #print(formatted_data)

    newdata = pd.DataFrame(formatted_data)
    newdata = newdata.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})


    #print(newdata.shape)
    #print(newdata)

    newdata.plot()


    #export the file to specific activity
    newdata.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1


x=1
for i in range(10):
    SAMPLE_RATE = 32

    PARTICIPANTE = x

    ATIVIDADE = 'AVD'
    MARCHA = 'G'
    SEQUENCIA = 5
    SENSOR = 'ACC'

    HEADER_LINES = 2

    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv') 
    #print('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv')
    #print('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv')

    #read file
    data = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/'+SENSOR+'.csv',index_col=False,header=None)
    data = data.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})
    init_time_measure = data.iloc[0,0]
    #print(data)

    #print(init_time_measure)


    #read tags that inform init and end of activity
    tags = pd.read_csv('Dataset/Participante '+str(PARTICIPANTE)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/tags.csv',index_col=False,header=None)
    #print(tags)
    #print(tags.shape)


    #store init and end activity time
    init_activ_time = tags.iloc[0,0]
    end_activ_time = tags.iloc[1,0]
    #print(init_activ_time)

    #calc time to cut in file init
    lines_to_cut_init = init_activ_time - init_time_measure
    #print(lines_to_cut_init)
    lines_to_cut_init = int(lines_to_cut_init*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_init)


    #calc time to cut in file end
    lines_to_cut_end = end_activ_time - init_time_measure
    #print(lines_to_cut_end)
    lines_to_cut_end = int(lines_to_cut_end*SAMPLE_RATE)+HEADER_LINES
    #print(lines_to_cut_end)


    #get only samples from init to end tagged activity
    formatted_data = data.iloc[lines_to_cut_init:lines_to_cut_end,:]

    #transform to real values according to Empatica Calc
    formatted_data = (formatted_data.values*2)/128

    #print(formatted_data)

    newdata = pd.DataFrame(formatted_data)
    newdata = newdata.rename(columns={0: 'acc_x', 1: 'acc_y', 2: 'acc_z'})


    #print(newdata.shape)
    #print(newdata)

    newdata.plot()


    #export the file to specific activity
    newdata.to_csv('Lifesenior/'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'/V'+str(PARTICIPANTE)+'_'+ATIVIDADE+'_'+MARCHA+'_'+str(SEQUENCIA)+'.csv', index=False)
    x+=1