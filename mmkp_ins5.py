import numpy as np
from mmkp import *

NUMBER_OF_ANTS = 10
N_ITERS = 50
ALPHA = 1.1
BETA = 1.5
RHO = 0.005
KP_FIRST = False
PLOT = True

c = [[1.2852865150998665, 21.174681295799306, 16.909142008572623], [27.96595210419219, 15.040457318525025, 27.018266600935142], [5.151470921564668, 13.39020439858612, 28.875972300713634], [15.162871981760782, 15.630209600667028, 9.755132585196485], [31.237191228931195, 30.608104922257535, 27.95608488763632], [35.02522099350806, 34.29699277473406, 21.341558709536784], [24.253188682583463, 6.076764982773564, 2.1004621660156344], [27.75080966279684, 16.453187201666164, 20.36086451570297], [32.91365099038018, 18.814031440769593, 33.45182053525097], [7.181714004836681, 3.4301531982259537, 3.9233274009253236], [31.809225786742267, 14.95083403730207, 24.985572564844283], [20.753191570022675, 0.8825643591403551, 23.50864157390111]]
p = [17, 28, 79, 58, 8, 69, 99, 59, 18, 29, 66, 13, 41, 41, 49, 64, 18, 19, 60, 97, 69, 79, 63, 32, 68, 71, 70, 96, 18, 25]
w = [[2.8890011012807393, 17.17707299523831, 15.657980391439558], [5.252683579061081, 11.350413101472059, 8.562824076117986], [14.714423217318974, 0.2917188060412901, 13.210186648651831], [14.759735119249314, 0.16961730174768874, 13.50750763372469], [19.638578551936142, 9.71613587764947, 13.985356451576475], [4.708890036593858, 2.5374281894708983, 9.816393311775043], [16.31269546449776, 13.11051584858509, 15.446875330212844], [10.6851823564266, 14.851089044392713, 13.131914121655779], [3.94993698236064, 5.901263604467044, 15.759991637064827], [2.983008365722699, 18.738926815884664, 17.819374741016006], [1.1208869363365115, 3.140101292536883, 15.156501418225943], [13.138362446703248, 19.614777761314198, 0.8218831867641008], [17.07305343568287, 11.6656848131604, 6.6949863940606535], [12.826254082233046, 3.8223232501574445, 18.868825393617332], [8.416338502111923, 10.627117995962783, 8.9180633175541], [14.947667949794798, 1.1395142915617362, 3.291607996749444], [12.7962833475034, 8.534657096306082, 2.6725767159974434], [7.332122069047273, 5.959355803190858, 1.777343282730195], [3.2463291272250827, 11.74636103196353, 15.973587164864174], [17.27399337113742, 13.718295537287107, 0.2337587829813459], [16.2473606336199, 10.355651048529573, 4.826186519972007], [7.045139033866727, 18.041286026498575, 10.176115167811012], [16.75705104704156, 19.92495690030214, 2.5975610411817818], [3.0794512210611025, 10.160426368168086, 1.4172541561508978], [1.547768588645848, 3.0678030256799804, 19.884048520480547], [13.953955316390378, 12.837541641019046, 3.0868747066475732], [12.452808615597089, 13.455841096342777, 12.9648652093559], [3.3211227443831537, 12.932978856430182, 13.170133823653229], [4.595797331879208, 8.15208250625343, 15.2460128416384], [14.580497327917062, 15.468398072248648, 2.2724002245355646]]

#print(np.sum(p))
acs_for_mmkp(p=p, c=c, w=w, n_ants=NUMBER_OF_ANTS, max_iter=N_ITERS, alpha=ALPHA, beta=BETA, rho=RHO, kp_first=KP_FIRST, plot=PLOT)
