from DictionarySetUp import dictionaryBuilder
from MatchToken import tokenMatch
from evaluator import evaluate
import time

HDFS_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
Andriod_format = '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>' #Andriod log format
Spark_format = '<Date> <Time> <Level> <Component>: <Content>'#Spark log format
Zookeeper_format = '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>' #Zookeeper log format
Windows_format = '<Date> <Time>, <Level>                  <Component>    <Content>' #Windows log format
Thunderbird_format = '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>' #Thunderbird_format
Apache_format = '\[<Time>\] \[<Level>\] <Content>' #Apache format
BGL_format = '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>' #BGL format
Hadoop_format = '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>' #Hadoop format
HPC_format = '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>' #HPC format
Linux_format = '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>' #Linux format
Mac_format = '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>' #Mac format
OpenSSH_format = '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>' #OpenSSH format
OpenStack_format = '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>' #OpenStack format
HealthApp_format = '<Time>\|<Component>\|<Pid>\|<Content>'
Proxifier_format = '\[<Time>\] <Program> - <Content>'

HDFS_Regex = [
        r'blk_(|-)[0-9]+' , # block id
        r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
        r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
]
Hadoop_Regex = [r'(\d+\.){3}\d+']
Spark_Regex = [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+']
Zookeeper_Regex = [r'(/|)(\d+\.){3}\d+(:\d+)?']
BGL_Regex = [r'core\.\d+']
HPC_Regex = [r'=\d+']
Thunderbird_Regex = [r'(\d+\.){3}\d+']
Windows_Regex = [r'0x.*?\s']
Linux_Regex = [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}']
Andriod_Regex = [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b']
Apache_Regex = [r'(\d+\.){3}\d+']
OpenSSH_Regex = [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+']
OpenStack_Regex = [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+']
Mac_Regex = [r'([\w-]+\.){2,}[\w-]+']
HealthApp_Regex = []
Proxifier_Regex = [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B']

# max = 0
# maxd = 1
# maxt = 1
#
# for t in range(1,101):
#     for d in range(t,101):
#         doubleDictionaryList, triDictionaryList, allTokenList = dictionaryBuilder(Andriod_format, 'TestLogs/Andriod_2k.log', Andriod_Regex)
#         tokenMatch(allTokenList,doubleDictionaryList,triDictionaryList,d,t,'Output/')
#         f_measure, accuracy = evaluate('GroundTruth/Andriod_2k.log_structured.csv', 'Output/event.csv')
#         if accuracy > max or max == 0:
#             max = accuracy
#             maxd = d
#             maxt = t
#         doubleDictionaryList.clear()
#         triDictionaryList.clear()
#         allTokenList.clear()
#
# print(max)
# print(maxd)
# print(maxt)

settings = {
        'Andriod_2k': {
            'log_format': Andriod_format,
            'rex': Andriod_Regex,
            'dt': 14,
            'tt': 13,
        },
        'Apache_2k': {
            'log_format': Apache_format,
            'rex': Apache_Regex,
            'dt': 75,
            'tt': 32,
        },
        'BGL_2k': {
                'log_format': BGL_format,
                'rex': BGL_Regex,
                'dt': 18,
                'tt': 10,
        },
        'HDFS_2k': {
                    'log_format': HDFS_format,
                    'rex': HDFS_Regex,
                    'dt': 15,
                    'tt':15,
                    },
    'Hadoop_2k': {
        'log_format': Hadoop_format,
        'rex': Hadoop_Regex,
        'dt': 9,
        'tt': 6,
    },
    'HealthApp_2k': {
        'log_format': HealthApp_format,
        'rex': HealthApp_Regex,
        'dt': 23,
        'tt': 5,
    },
    'HPC_2k': {
        'log_format': HPC_format,
        'rex': HPC_Regex,
        'dt': 13,
        'tt': 11,
    },
    'Linux_2k': {
        'log_format': Linux_format,
        'rex': Linux_Regex,
        'dt': 32,
        'tt': 24,
    },
    'Mac_2k': {
        'log_format': Mac_format,
        'rex': Mac_Regex,
        'dt': 11,
        'tt': 10,
    },
    'OpenSSH_2k': {
        'log_format': OpenSSH_format,
        'rex': OpenSSH_Regex,
        'dt': 47,
        'tt': 80,
    },
    'OpenStack_2k': {
        'log_format': OpenStack_format,
        'rex': OpenStack_Regex,
        'dt': 16,
        'tt': 9,
    },
    'Proxifier_2k': {
        'log_format': Proxifier_format,
        'rex': Proxifier_Regex,
        'dt': 115,
        'tt': 95,
    },
    'Spark_2k': {
        'log_format': Spark_format,
        'rex': Spark_Regex,
        'dt': 37,
        'tt': 37,
    },
    'Thunderbird_2k': {
        'log_format': Thunderbird_format,
        'rex': Thunderbird_Regex,
        'dt': 8,
        'tt': 7,
    },
    'Windows_2k': {
        'log_format': Windows_format,
        'rex': Windows_Regex,
        'dt': 16,
        'tt': 16,
    },
    'Zookeeper_2k': {
        'log_format': Zookeeper_format,
        'rex': Zookeeper_Regex,
        'dt': 9,
        'tt': 9,
    },
}

for key in ['HealthApp_2k']:
# for key in settings.keys():
    name = key
    log_format=settings[key]['log_format']
    rex = settings[key]['rex']
    doubleThreshold = settings[key]['dt']
    triThreshold = settings[key]['tt']
    start = time.perf_counter()
    doubleDictionaryList, triDictionaryList, allTokenList = dictionaryBuilder(log_format, 'TestLogs/{}.log'.format(name), rex)
    tokenMatch(allTokenList,doubleDictionaryList,triDictionaryList,doubleThreshold,triThreshold,'Output/{}'.format(name))
    end = time.perf_counter()
    interval = end - start
    print("{} spent time {}".format(name, interval))

    f_measure, accuracy = evaluate('GroundTruth/{}.log_structured.csv'.format(name), 'Output/{}Event.csv'.format(name))


#We use an automatic approach to gain the threshold. The parameters listed below are suggested thresholds for different datasets.

#Andriod: 14, 13					
#Apache: 75, 32
#BGL: 18, 10						
#HDFS: 15, 15						
#Hadoop: 9, 6						
#HPC: 13, 11						
#Linux: 32, 24						
#Mac: 11, 10						
#OpenSSH: 47, 80					
#OpenStack: 16, 9					
#Proxifier: 115, 95					
#Spark: 37, 37						
#Thunderbird: 8, 7					
#Windows: 16, 16					
#Zookeeper: 9, 9					
#HealthApp: 23, 5

"""
output:
Andriod_2k spent time 0.091192559
Precision: 0.9588, Recall: 0.9847, F1_measure: 0.9716, Parsing_Accuracy: 0.7895
Apache_2k spent time 0.05060920300000005
Precision: 1.0000, Recall: 0.4684, F1_measure: 0.6380, Parsing_Accuracy: 0.3125
BGL_2k spent time 0.06568648200000005
Precision: 0.9858, Recall: 0.9414, F1_measure: 0.9631, Parsing_Accuracy: 0.6450
HDFS_2k spent time 0.07954166699999998
Precision: 1.0000, Recall: 0.9816, F1_measure: 0.9907, Parsing_Accuracy: 0.9400
Hadoop_2k spent time 0.06955664300000008
Precision: 0.9978, Recall: 0.6372, F1_measure: 0.7777, Parsing_Accuracy: 0.4280
HealthApp_2k spent time 0.02976697500000003
Precision: 0.9984, Recall: 0.4168, F1_measure: 0.5881, Parsing_Accuracy: 0.2775
HPC_2k spent time 0.03284425599999974
Precision: 0.9988, Recall: 0.9890, F1_measure: 0.9939, Parsing_Accuracy: 0.9055
Linux_2k spent time 0.07024956599999976
Precision: 0.9679, Recall: 0.1461, F1_measure: 0.2539, Parsing_Accuracy: 0.1460
Mac_2k spent time 0.10190859499999982
Precision: 0.7752, Recall: 0.9264, F1_measure: 0.8441, Parsing_Accuracy: 0.5195
OpenSSH_2k spent time 0.08731066499999995
Precision: 0.9999, Recall: 0.9309, F1_measure: 0.9641, Parsing_Accuracy: 0.4290
OpenStack_2k spent time 0.10709795100000008
Precision: 1.0000, Recall: 0.5745, F1_measure: 0.7298, Parsing_Accuracy: 0.2350
Proxifier_2k spent time 0.09412476400000003
Precision: 0.9980, Recall: 0.2886, F1_measure: 0.4477, Parsing_Accuracy: 0.0265
Spark_2k spent time 0.0879804420000001
Precision: 0.9887, Recall: 0.4056, F1_measure: 0.5752, Parsing_Accuracy: 0.3805
Thunderbird_2k spent time 0.07593716800000028
Precision: 0.9852, Recall: 0.3561, F1_measure: 0.5231, Parsing_Accuracy: 0.1875
Windows_2k spent time 0.05977846999999947
Precision: 0.9995, Recall: 0.8415, F1_measure: 0.9137, Parsing_Accuracy: 0.6940
Zookeeper_2k spent time 0.0513348149999997
Precision: 0.9995, Recall: 0.8591, F1_measure: 0.9240, Parsing_Accuracy: 0.7235

Accuracy compare with logpai/drain: 

|             | logram | drain  |
| ----------- | ------ | ------ |
| Andriod     | 0.7895 | 0.911  |
| Apache      | 0.3125 | 1      |
| BGL         | 0.645  | 0.9625 |
| Hadoop      | 0.428  | 0.9475 |
| HDFS        | 0.94   | 0.9975 |
| HealthApp   | 0.2775 | 0.78   |
| HPC         | 0.9055 | 0.887  |
| Linux       | 0.146  | 0.69   |
| Mac         | 0.5195 | 0.7865 |
| OpenSSH     | 0.429  | 0.7875 |
| OpenStack   | 0.235  | 0.7325 |
| Proxifier   | 0.0265 | 0.5265 |
| Spark       | 0.3805 | 0.92   |
| Thunderbird | 0.1875 | 0.955  |
| Windows     | 0.694  | 0.997  |
| Zookeeper   | 0.7235 | 0.9665 |

"""




