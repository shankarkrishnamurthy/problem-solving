class Solution(object):
    def wordBreak_ispossible(self, str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def do_wb(s,e):
            for i in range(s,e):
                for j in range(i):
                    if wd.has_key(str[j:i]) and dp[j]:
                        dp[i] = True
                        break
            return dp[e-1]

        l = len(str)
        wd = dict([(v,1) for v in wordDict])
        dp = [False]*(l+1)
        dp[0] = True
        return do_wb(0,l+1)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        l = len(s)
        wd = dict([(v,1) for v in wordDict])
        s1 = set(s)
        ss = set(''.join(wordDict))
        if len(s1-ss) > 0:
            return []
        if len(set(s))< 5 and len(s) > 50:
            s1 = self.wordBreak_ispossible(s,wordDict)
            if not s1:
                return []
        dp = [False]*(l+1)
        dp[0] = True
        res = [ [] for i in range(l+1) ]
        for i in range(0,l+1):
            for j in range(i):
                if wd.has_key(s[j:i]) and dp[j]:
                    dp[i] = True
                    if j == 0:
                        res[i] = [s[j:i]]
                    else:
                        for v in res[j]:
                            res[i].append(v + " " + s[j:i])
        return res[l]
        
print Solution().wordBreak("a", ["b"])
print Solution().wordBreak("x", ["x"])
print Solution().wordBreak("leetcode", ["leet", "code", "le", "etc", "ode"])
print Solution().wordBreak("agflm", ["a", "gf", "lm", "gfl", "l", "m"])
print Solution().wordBreak("angflm", ["a", "gf", "lm", "gfl", "l"])
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])
print Solution().wordBreak( "fkjjlbhkbbefinemajmoebhjbkojmcaehiibankkomghncojbjgedebjfdocjhclmbalebladkcaidacaiiokemdmaabjalmbgggjjfjfedegmnkidceogjdgncmlhodkcmjkfolgfnaklkjbocjhhakgmigkcmilbikbhjcgz", ["gaggkdeo","igkcmil","mfljaieijcjk","nddenji","ihkao","k","halnhbcmabjb","aeb","hmamkhmlfce","mnkjgjjodida","gm","hancobi","g","hmoafjnono","meanolmbloog","nochomliagledo","ahdimafaacc","necn","goicmonlkil","jfigiglloi","jjfjfede","akgjlbgjldec","oooij","dk","elbofj","mmddfkfig","kaklf","bcbeenfeee","ajkooijb","oaanehdai","e","omk","mfmed","iheidmbjeinfebk","bikbhjcg","eh","hmbneijnk","cccganlndjo","igfmdoiihc","edoncgeohal","i","glie","ncojbjg","gnmifoifaec","ncogocd","kgogljaidon","dkghjha","mf","fmoimobjf","incmj","ihiehafnmilce","hji","daoklglc","obbomj","fh","f","mnmbhk","jaj","ikbdlhfhk","lihmboinijkkka","cda","boimoc","iohgjocn","gaof","lld","jhhak","jhjekma","jedihdccoojide","anibenolmjmbf","ofhaicalhmdcnjd","c","egonomcienfh","ml","lgekjonkeao","ddhahngil","gfmcb","oiikakdhl","iab","jehicc","jmocmaiokn","eflmhnglhejd","ahii","dmo","dfdgfnmldhaooae","nohgoc","jjlmggdbhno","odkimohjodbh","dmhkkgjcjhiid","fcdgbjgbbm","mhoomlad","nbofdoofom","cencoc","aefehagm","nnio","jjiigmc","cgel","ela","hhd","jkkddacaam","b","mo","md","damiock","ebeao","mlffgmgbloc","abgmmnmiijglm","ibjdnckgfonia","nn","mnc","hijgoeco","jkgaghmhlnehc","ieadnfjcoi","kmjfnjhlabcihe","gobkj","cmajffc","hhbmckl","fgmghbh","ehclhidfbfb","nibjmglgmglhf","hnblghaejege","nkkomgh","fbkfl","ogdail","ejehdmbk","mocmnio","mlfkgaab","dijb","mlbcnljogof","lnjadlm","ijgcicndm","cgnblkchngklbf","jbebfgk","hdjg","dl","honjckb","cdomnnhjocaoe","ebnje","igkgjalnbhinghi","iojginhi","fmmdnnjobikond","jeflgnl","noodabd","ojgd","nfkjdggjn","kajbdaikidneidm","klbjfcfjlkcibba","geecdcfbkede","ndjbgdadje","mokfehacdd","mjdkenofkaeli","mcmnj","mfggccd","nmonjefcjolhfgg","amdfecagjfkfdh","kbijncaeoon","febfhfjgkhdab","bgglmgmkjhne","mhhojoihflf","dfaffjcdnchb","mnh","fjcikedcd","odd","j","kjafgaiklcemkcd","lnhgochigmcgk","fnhijgnend","gniekccclcn","ofggcjlidbjeh","aojegacnehgbdgc","bbabogkdekleei","egcmokhdio","inl","fleeid","mmdcekhihfc","ckbbhaaoakfe","nadbaeddfjej","finiacgd","khid","haaiani","hekleijlafocdh","jihfh","aolhnacokig","nnggoafjl","fkhjghiaeojhi","oan","aajimcikcnaebe","achigecoboif","cjhed","ijhg","oonjh","allhnelgjdl","abh","cabncchfmbn","khnciickdoehol","jnof","bfmalenhf","bckmd","haln","iaiffadaadji","hoadjf","nagchlghjhk","hjlbacedkkdnk","ace","bmldoimodegcl","mdiojfhgmfg","omkblifelkfifjn","amnldcmobkkjmkj","iaibe","efnn","nmbf","a","foenajo","jgnkhn","ncagcgnfcfm","confnibafdeiiad","cdjgakfn","lmh","nlabndn","n","kc","gddjoojoeomanj","kmf","hj","jgnijhekbmbcbk","gjhfei","bfiladjlggjjh","fckgfmdeikdkkfi","abnldlg","fgnnjefaegg","mochafeafehelb","ncbdkecddnegbko","ceedljkegf","okhdgjkao","dfdcocheclaaj","ladkcaida","klfkbnbjeg","bihmahlknalkbb","gobo","edggcafghgbokfg","lfcdahkamfnnlbe","fhobdnbh","fllibcljdmajn","obhlnghf","njbcm","kmkbnlldhadfc","ghmk","ijbeihkojjml","clmbaleb","offmicbgejkh","hmmjfbkh","jkfehdlek","gbk","gmocchifcgmofhd","lbc","anicc","ejhddgheln","nemajmoebhjbkoj","naemi","nnenmabkhlm","bjhb","jmjhmnjkgh","admjcjbca","llem","hkbbe","nmdjmkjhdja","koniblnljgmmbbg","biljfalmflchb","dblnhfib","ok","emilcjdncm","ilfkbiodab","eoohdfhno","dgd","o","mbjj","legdidaoclb","nghlkbkbbljh","ekabk","ggkgfkbomme","ogfmlfcaklef","ikgg","kghbdjieniho","noighlblehf","jfmgihkonmbm","bimicdfhlifg","klimcfnojbiooc","lakbda","mkcoboaddi","nfaebmd","fbjlahcaajamjaj","gncllkii","fboglhliehal","jk","ocimnaceklgmoe","fcnh","ohcnnkamoaom","ccimaiofdealnjf","mkdanlkeekecc","hamboelbcdbai","lbljfeianmkhon","bhjbndfffcdhm","nafgoeceilmebn","jmb","fmmfmdmnigllb","dbaobkconcfcan","ajdibacdfg","iknhfe","abdaeca","l","becafg","eeieaeoiaagjbdi","odgfeca","anbceegkdn","bknkeonigb","fj","kacanki","jlkoncijbo","kaeobkadncbgn","eagocnmnjjhnlmh","adnnllieng","imlkbgfmolmj","nlmnkngheaof","kcockjm","ggmfbilldo","abagjicencjdhh","gedckmkehn","ijecleakkbndgl","joifkiccb","aiameogbecidakj","jdaiilnfh","kgdond","bnecbmebab","mfmlijibjdcoddh","nlcbiiejklclf","jlijddomde","gniiehcllnm","amj","fbcclace","ainmcmmhbc","cglfdaklhmmocl","hfkfdfkmlkai","hkfjjhejacc","kgm","anbhgnjhjfabiok","bdhmgigjbj","dokmfnldohbgk","cg","bgmkhfd","dfj","gjhd","idkmgmmnaejkdel","gekmbmmn","hccecjfbfij","cfek","fjeoegjlmligac","alhnjlacob","liedbjcj","adlif","okddmo","lgbkmbek","oobncia","moobambifbljk","gakogkghmihooak","hllhgdamoiej","lfkjddl","mjfb","ibngnkbicenfga","dombgn","kjboc","hdamjncmdol","hicl","obocccgm","ccomeiofkjnknga","acflfadojem","kl","odkcmjkfolgfnak","jlennlehfii","biimao","ghmaeadafbj","coggdjg","cdnchammeiegom","lofmfgelbmlehnc","jialklmcdlohkm","jbimboeijnbmgol","nndgm","hebjao","cijlobchgka","hljojiclje","gdb","kamgaigodfcbk","mi","lcjalnfojcmjbl","mdkmocngibmgnjb","fobhhgdf","dekdcobbeghi","elofjhgeackijdk","abjal","glnnkdccgi","kbcjlljgdnnbmi","bg","jnoffjafmaa","h","knhefdjjlaife","nbalab","jkhd","neaofeanlcidni","bdckcnlkbo","fkj","ihlknj","iggdjfk","nmmkjg","jhmimaem","minieag","fofgj","jafebbgi","cbanbcaknggl","nkncbcjlidilefo","filngail","oocb","hdhliiikjfhm","hfmaiekfb","af","hfjemfchd","hainei","mehfggjbghiomni","lcjnmbclgbin","djeokdahia","lh","lfbfoj","aohgcfcmbhmek","clfbgjichnmfa","chieogij","fglg","accifaokkgmnb","iamjljccnihcn","idocdnlj","dh","clhmcifbgcjf","bjmlcfhdjocgl","nbhajeoi","adeaadndhie","mlheaedi","jdbgkfadelbejhg","ohlecggkboamn","boinmneifn","angj","hoclbcdofng","gkjcegiifa","lakke","gfa","nnimh","iikjgcmfbagd","fefgjd","eeboefdackceb","mmkccjei","hloiook","hcge","gmhncohdjkk","clmkcojajn","ogjdgncmlh","dfookkmceiigmh","fhkjcimkiofoinn","mjahgdgnabdj","hb","obkkbdcjglm","le","cmninbjdhekcb","oodikoamlelcne","bnbafkkddmk","neagoocl","bhmdmlejaiji","mjlbealgl","cafnnmniln","labfg","leelb","ocifbibijfgdk","dbbb","ghbmcg","mom","igo","jcmfoebajefjdi","iikgmjn","obnckkadabjhfi","lhekmhildjkcn","njfogfnj","fcgacdhcclde","ichaeligmk","hmcjoigoea","cc","ickfcelfilkbk","ch","jkakkdlh","fkjjlb","dkcknlo","lc","nklohjhjif","jhgkjjfcjefc","kalkc","meglmnhlnem","lnbmmcbdgfkeem","ejkbobfilcnafel","lk","jlbncfd","eblmooggngamof","okmmomdmief","dahc","ackmjhnmfgaoafa","fmjgi","dbmflmfkdia","aeajncek","ehalibdilikeok","mnjojhdjngin","m","hfdlmjjcfmacb","ekciad","dkdfmnieiahio","nihfnbekbhk","okj","mmjf","anfjk","kocaoh","amfcflnla","jealekjf","fgokkddmfa","ffbbabn","okldhifhnhbm","edmaga","ajahiocomhbablk","danmbn","ilcjcheddnabll","ochfblfeldbo","ignhkon","meiailaib","aheodadm","dec","ianoghmba","bni","cenegah","jcnkiciendihdih","kegkcmnkh","fi","aeldnnmcbilelg","emejaicfjhafod","jjonddlecfgdm","elkcmmlfbiemeg","edebjfdocjh","ankghmibmgd","afmmgmi","afliaf","aecckchdf","mcnhfojki","la","blbaif","bifj","nkidce","ddhigddihlkm","bgjnn","haclkkjbjdjn","mcaehiiba","iebnfadil","kfgjab","bafdkg","gnbbgilljiacl","fdajjg","caiiokemdma","adfchcjninhho","meaaf","jahifegbhjj","hbhgkdl","egomnbc","ooccmbmicehi","afaecdcbjgf","mcaedecih","ihjnbgacjahfmj","hcnco","hbecolgk","jdknfnmjehoc","mnmbndjkono","mk","kmmcjjeab","lekbo","mcbaknmkcnebj","mbggg","men","jn","hgcchmkje","ncnlijanmcog","hll","jlhkhiggelnkhbk","bnoaah","enainmmdaamaicn","jieio","anadihbcbg","ligl","fmjkjmgmjmlonel","gifkkbkedeno","hmklhikf","jeoll","kbhi","cnkihoga","ihkndcibcgl","deogdlmcbc","mocghlg","gkaihhoa","miibddoebolibnc","ggecjoiodklb","nafdahhn","meboilne","olkhhkledm","hdklcdfmne","aclj","migeheccjgod","cejnilnhfadml","mfkmacdgomhcalm","faijmldniblnl","mmfcln","lhmdehaho","hcj","fkconhlmknloccn","hckhl","lheki","blenkofhj","bhjjgkmblen","dndjigjgikb","jnjamjglhim","hg","bnlbgllnkfemfgj","ll","hjekhnhnoam","mldahadgmegj","dmj","henklighfkah","lcl","lobhgifjflgcicc","chnfjdeije","jbaedijcdm","jcinegma","oojiijjcdh","bkejicnojmlj","jncnoc","embdomh","chkjonad","eekgln","aodogkkmodaoc","ee","ngnmdfldf","eajlnmjeckeek","lnnaiggam","hlohol","nibflancimmfk"])

