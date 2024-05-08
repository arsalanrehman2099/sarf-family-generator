word_before_isms = 'فَهُوَ'
word_for_commanding = 'الأَمْرُ مِنْهُ'
word_for_forbidding = 'وَالنَّهْىُ عَنْهُ'
word_for_forbidding2 = ' لَا'
word_for_time_place = 'وَالظَّرْفُ مِنْهُ'

################################################################
######################### BIG FAMILIES #########################
################################################################

# 01: Aslama Family
def aslama_family(F='س',I='ل',L='م'):
    aslama = {}
    
    aslama['past'] = f"أَ{F}ْ{I}َ{L}َ"
    aslama['pres'] = f"يُ{F}ْ{I}ِ{L}ُ"
    aslama['masdar'] = f"إِ{F}ْ{I}َا{L}ًا"
    aslama['ism_fail'] = f"مُ{F}ْ{I}ِ{L}ٌ"

    aslama['past_passive'] = f"اُ{F}ْ{I}ِ{L}َ"
    aslama['pres_passive'] = f"يُ{F}ْ{I}َ{L}ُ"
    aslama['ism_mafool'] = f"مُ{F}ْ{I}َ{L}ٌ"

    aslama['commanding'] = f"أَ{F}ْ{I}ِ{L}ْ"
    aslama['forbidding'] = f"تُ{F}ْ{I}ِ{L}ْ"
    aslama['time_place'] = f"مُ{F}ْ{I}َ{L}ٌ"
    
    return aslama

# 02: Allama Family
def allama_family(F='ع',I='ل',L='م'):
    allama = {}
    
    allama['past'] = f"{F}َ{I}َّ{L}َ"
    allama['pres'] = f"يُ{F}َ{I}ِّ{L}ُ"
    allama['masdar'] = f"تَ{F}ْ{I}ِيْ{L}ًا"
    allama['ism_fail'] = f"مُ{F}َ{I}ِّ{L}ٌ"

    allama['past_passive'] = f"{F}ُ{I}ِّ{L}َ"
    allama['pres_passive'] = f"يُ{F}َ{I}َّ{L}ُ"
    allama['ism_mafool'] = f"مُ{F}َ{I}َّ{L}ٌ"

    allama['commanding'] = f"{F}َ{I}ِّ{L}ْ"
    allama['forbidding'] = f"تُ{F}َ{I}ِّ{L}ْ"
    allama['time_place'] = f"مُ{F}َ{I}َّ{L}ٌ"
    
    return allama

# 03: Jaahada Family
def jahaada_family(F='ج',I='ه',L='د'):
    jahaada = {}
    
    jahaada['past'] = f"{F}َا{I}َ{L}َ"
    jahaada['pres'] = f"يُ{F}َا{I}ِ{L}ُ"
    jahaada['masdar'] = f"{F}ِ{I}َا{L}ًا ومُ{F}َا{I}َ{L}َةً"
    jahaada['ism_fail'] = f"مُ{F}َا{I}ِ{L}ٌ"

    jahaada['past_passive'] = f"{F}ُو{I}ِ{L}َ"
    jahaada['pres_passive'] = f"يُ{F}َا{I}َ{L}ُ"
    jahaada['ism_mafool'] = f"مُ{F}َا{I}َ{L}ٌ"

    jahaada['commanding'] = f"{F}َا{I}ِ{L}ْ"
    jahaada['forbidding'] = f"تُ{F}َا{I}ِ{L}ْ"
    jahaada['time_place'] = f"مُ{F}َا{I}َ{L}ٌ"
    
    return jahaada

# 04: Ta'allama Family
def taallama_family(F='ع',I='ل',L='م'):
    taallama = {}
    
    taallama['past'] = f"تَ{F}َ{I}َّ{L}َ"
    taallama['pres'] = f"يَتَ{F}َ{I}َّ{L}ُ"
    taallama['masdar'] = f"تَ{F}َ{I}ُّ{L}ًا"
    taallama['ism_fail'] = f"مُتَ{F}َ{I}ِّ{L}ٌ"

    taallama['past_passive'] = f"تُ{F}ُ{I}ِّ{L}َ"
    taallama['pres_passive'] = f"يُتَ{F}َ{I}َّ{L}ُ"
    taallama['ism_mafool'] = f"مُتَ{F}َ{I}َّ{L}ٌ"

    taallama['commanding'] = f"تَ{F}َ{I}َّ{L}ْ"
    taallama['forbidding'] = f"تَتَ{F}َ{I}َّ{L}ْ"
    taallama['time_place'] = f"مُتَ{F}َ{I}َّ{L}ٌ"
    
    return taallama

# 05: Tasa'ala Family
def tasaala_family(F='س',I='ء',L='ل'):
    tasaala = {}
    
    tasaala['past'] = f"تَ{F}َا{I}َ{L}َ"
    tasaala['pres'] = f"يَتَ{F}َا{I}َ{L}ُ"
    tasaala['masdar'] = f"تَ{F}َا{I}ُ{L}ًا"
    tasaala['ism_fail'] = f"مُتَ{F}َا{I}ِ{L}ٌ"

    tasaala['past_passive'] = f"تُ{F}ُو{I}ِ{L}َ"
    tasaala['pres_passive'] = f"يُتَ{F}َا{I}َ{L}ُ"
    tasaala['ism_mafool'] = f"مُتَ{F}َا{I}َ{L}ٌ"

    tasaala['commanding'] = f"تَ{F}َا{I}َ{L}ْ"
    tasaala['forbidding'] = f"تَتَ{F}َا{I}َ{L}ْ"
    tasaala['time_place'] = f"مُتَ{F}َا{I}َ{L}ٌ"
    
    return tasaala

# 06: Inqalaba Family
def inqalaba_family(F='ق',I='ل',L='ب'):
    inqalaba = {}
    
    inqalaba['past'] = f"اِنْ{F}َ{I}َ{L}َ"
    inqalaba['pres'] = f"يَنْ{F}َ{I}ِ{L}ُ"
    inqalaba['masdar'] = f"اِنْ{F}ِ{I}َا{L}ًا"
    inqalaba['ism_fail'] = f"مُنْ{F}َ{I}ِ{L}ٌ"

    inqalaba['commanding'] = f"اِنْ{F}َ{I}ِ{L}ْ"
    inqalaba['forbidding'] = f"تَنْ{F}َ{I}ِ{L}ْ"
    inqalaba['time_place'] = f"مُنْ{F}َ{I}َ{L}ٌ"

    return inqalaba

# 07: Iqtaraba Family
def iqtaraba_family(F='ق',I='ر',L='ب'):
    iqtaraba = {}
    
    iqtaraba['past'] = f"اِ{F}ْتَ{I}َ{L}َ"
    iqtaraba['pres'] = f"يَ{F}ْتَ{I}ِ{L}ُ"
    iqtaraba['masdar'] = f"اِ{F}ْتِ{I}َا{L}ًا"
    iqtaraba['ism_fail'] = f"مُ{F}ْتَ{I}ِ{L}ٌ"

    iqtaraba['past_passive'] = f"اُ{F}ْتُ{I}ِ{L}َ"
    iqtaraba['pres_passive'] = f"يُ{F}ْتَ{I}َ{L}ُ"
    iqtaraba['ism_mafool'] = f"مُ{F}ْتَ{I}َ{L}ٌ"

    iqtaraba['commanding'] = f"اِ{F}ْتَ{I}ِ{L}ْ"
    iqtaraba['forbidding'] = f"تَ{F}ْتَ{I}ِ{L}ْ"
    iqtaraba['time_place'] = f"مُ{F}ْتَ{I}َ{L}ٌ"
    
    return iqtaraba

# 08: Istagfara Family
def istagfara_family(F='غ',I='ف',L='ر'):
    istagfara = {}
    
    istagfara['past'] = f"اِسْتَ{F}ْ{I}َ{L}َ"
    istagfara['pres'] = f"يَسْتَ{F}ْ{I}ِ{L}ُ"
    istagfara['masdar'] = f"اِسْتِ{F}ْ{I}َا{L}ًا"
    istagfara['ism_fail'] = f"مُسْتَ{F}ْ{I}ِ{L}ٌ"

    istagfara['past_passive'] = f"اُسْتُ{F}ْ{I}ِ{L}َ"
    istagfara['pres_passive'] = f"يُسْتَ{F}ْ{I}َ{L}ُ"
    istagfara['ism_mafool'] = f"مُسْتَ{F}ْ{I}َ{L}ٌ"

    istagfara['commanding'] = f"اِسْتَ{F}ْ{I}ِ{L}ْ"
    istagfara['forbidding'] = f"تَسْتَ{F}ْ{I}ِ{L}ْ"
    istagfara['time_place'] = f"مُسْتَ{F}ْ{I}َ{L}ٌ"
    
    return istagfara


################################################################
######################## SMALL FAMILIES ########################
################################################################

# 01: Nasara Family
def nasara_family(f = 'ن', i = 'ص', l = 'ر'):
    nasara = {}
    
    past = f"{f}َ{i}َ{l}َ"
    pres = f"يَ{f}ْ{i}ُ{l}ُ"
    masdar = f"{f}ُ{i}ْ{l}َةً"
    ism_fail = f"{f}َا{i}ِ{l}ٌ"

    past_passive = f"{f}ُ{i}ِ{l}َ"
    pres_passive = f"يُ{f}ْ{i}َ{l}ُ"
    ism_mafool = f"مَ{f}ْ{i}ُو{l}ٌ"

    commanding = f"اُ{f}ْ{i}ُ{l}ْ"
    forbidding = f"تَ{f}ْ{i}ُ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    nasara['past'] = past
    nasara['pres'] = pres
    nasara['masdar'] = masdar
    nasara['ism_fail'] = ism_fail

    nasara['past_passive'] = past_passive
    nasara['pres_passive'] = pres_passive
    nasara['ism_mafool'] = ism_mafool

    nasara['commanding'] = commanding
    nasara['forbidding'] = forbidding
    nasara['time_place'] = time_place
    
    return nasara

# 02: Fataha Family
def fataha_family(f = 'ف', i = 'ت', l = 'ح'):
    fataha = {}
    
    past = f"{f}َ{i}َ{l}َ"
    pres = f"يَ{f}ْ{i}َ{l}ُ"
    masdar = f"{f}َ{i}ْ{l}ًا"
    ism_fail = f"{f}َا{i}ِ{l}ٌ"

    past_passive = f"{f}ُ{i}ِ{l}َ"
    pres_passive = f"يُ{f}ْ{i}َ{l}ُ"
    ism_mafool = f"مَ{f}ْ{i}ُو{l}ٌ"

    commanding = f"اِ{f}ْ{i}َ{l}ْ"
    forbidding = f"تَ{f}ْ{i}َ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    fataha['past'] = past
    fataha['pres'] = pres
    fataha['masdar'] = masdar
    fataha['ism_fail'] = ism_fail

    fataha['past_passive'] = past_passive
    fataha['pres_passive'] = pres_passive
    fataha['ism_mafool'] = ism_mafool

    fataha['commanding'] = commanding
    fataha['forbidding'] = forbidding
    fataha['time_place'] = time_place
    
    return fataha

# 03: Dharaba Family
def dharaba_family(f = 'ض', i = 'ر', l = 'ب'):
    dharaba = {}
    
    past = f"{f}َ{i}َ{l}َ"
    pres = f"يَ{f}ْ{i}ِ{l}ُ"
    masdar = f"{f}َ{i}ْ{l}ًا"
    ism_fail = f"{f}َا{i}ِ{l}ٌ"  

    past_passive = f"{f}ُ{i}ِ{l}َ" 
    pres_passive = f"يُ{f}ْ{i}َ{l}ُ"  
    ism_mafool = f"مَ{f}ْ{i}ُو{l}ٌ" 

    commanding = f"اِ{f}ْ{i}ِ{l}ْ"
    forbidding = f"تَ{f}ْ{i}ِ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    dharaba['past'] = past
    dharaba['pres'] = pres
    dharaba['masdar'] = masdar
    dharaba['ism_fail'] = ism_fail

    dharaba['past_passive'] = past_passive
    dharaba['pres_passive'] = pres_passive
    dharaba['ism_mafool'] = ism_mafool

    dharaba['commanding'] = commanding
    dharaba['forbidding'] = forbidding
    dharaba['time_place'] = time_place
    
    return dharaba

# 04: Samiaa Family
def samiaa_family(f = 'س', i = 'م', l = 'ع'):
    samiaa = {}
    
    past = f"{f}َ{i}ِ{l}َ"
    pres = f"يَ{f}ْ{i}َ{l}ُ"
    masdar = f"{f}َ{i}ْ{l}ًا"
    ism_fail = f"{f}َا{i}ِ{l}ٌ"  

    past_passive = f"{f}ُ{i}ِ{l}َ" 
    pres_passive = f"يُ{f}ْ{i}َ{l}ُ"  
    ism_mafool = f"مَ{f}ْ{i}ُو{l}ٌ" 

    commanding = f"اِ{f}ْ{i}َ{l}ْ"
    forbidding = f"تَ{f}ْ{i}َ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    samiaa['past'] = past
    samiaa['pres'] = pres
    samiaa['masdar'] = masdar
    samiaa['ism_fail'] = ism_fail

    samiaa['past_passive'] = past_passive
    samiaa['pres_passive'] = pres_passive
    samiaa['ism_mafool'] = ism_mafool

    samiaa['commanding'] = commanding
    samiaa['forbidding'] = forbidding
    samiaa['time_place'] = time_place
    
    return samiaa

# 05: Hasiba Family
def hasiba_family(f = 'ح', i = 'س', l = 'ب'):
    hasiba = {}

    past = f"{f}َ{i}ِ{l}َ"
    pres = f"يَ{f}ْ{i}ِ{l}ُ"
    masdar = f"{f}ِ{i}َا{l}ًا"
    ism_fail = f"{f}َا{i}ِ{l}ٌ"  

    past_passive = f"{f}ُ{i}ِ{l}َ" 
    pres_passive = f"يُ{f}ْ{i}َ{l}ُ"  
    ism_mafool = f"مَ{f}ْ{i}ُو{l}ٌ" 

    commanding = f"اِ{f}ْ{i}ِ{l}ْ"
    forbidding = f"تَ{f}ْ{i}ِ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    hasiba['past'] = past
    hasiba['pres'] = pres
    hasiba['masdar'] = masdar
    hasiba['ism_fail'] = ism_fail

    hasiba['past_passive'] = past_passive
    hasiba['pres_passive'] = pres_passive
    hasiba['ism_mafool'] = ism_mafool

    hasiba['commanding'] = commanding
    hasiba['forbidding'] = forbidding
    hasiba['time_place'] = time_place
    
    return hasiba

# 06: Karuma Family
def karuma_family(f = 'ك', i = 'ر', l = 'م'):
    karuma = {}
    
    past = f"{f}َ{i}ُ{l}َ"
    pres = f"يَ{f}ْ{i}ُ{l}ُ"
    masdar = f"{f}َ{i}َا{l}َةً"
    ism_fail = f"{f}َ{i}ِيْ{l}ٌ"  

    commanding = f"اُ{f}ْ{i}ُ{l}ْ"
    forbidding = f"تَ{f}ْ{i}ُ{l}ْ"
    time_place = f"مَ{f}ْ{i}َ{l}ٌ مَ{f}ْ{i}ِ{l}ٌ مَ{f}ْ{i}َ{l}َةٌ"
    
    karuma['past'] = past
    karuma['pres'] = pres
    karuma['masdar'] = masdar
    karuma['ism_fail'] = ism_fail

    karuma['commanding'] = commanding
    karuma['forbidding'] = forbidding
    karuma['time_place'] = time_place
    
    return karuma

