#########################
# Não cópia não, irmão. #
#########################
# Sim, os comandos tão  #
# tudo bagunçado.       # 
#########################

import os
import time

os.system("clear")

while True:
 print('''\033[0;35mEscolha o seu idioma. | Choose your language.
	
[ \033[m0\033[0;35m ] Português
[ \033[m1\033[0;35m ] English\033[m''')
 Idioma = int(input('>> \033[0;33m'))
 os.system("clear")
 time.sleep(0.5)
 if Idioma == 0:
  while True:  
   print('''\033[0;35m[ \033[m0\033[0;35m ] Começar
      
[ \033[m98\033[0;35m ] Idioma
[ \033[m99\033[0;35m ]\033[m \033[0;31mSair\033[m''')
   opção = int(input('>> \033[0;33m'))
   if opção == 0:
      os.system("clear")
      print('\033[0;35mOk, vamos começar\033[m')
      time.sleep(2)
      os.system("clear")
      print('''\033[7;35mQuestão 1\033[m

\033[0;35mQuando foi a segunda guerra mundial?
          
[ \033[m0\033[0;35m ] 1914
[ \033[m1\033[0;35m ] 1976
[ \033[m2\033[0;35m ] 1854
[ \033[m3\033[0;35m ] 1939\033[m''')
      Qfasgm = int(input('>> \033[0;33m'))
      if Qfasgm == 3:
         os.system("clear")
         print('''\033[7;32mAcertou :D\033[m''')
         time.sleep(1.5)
         os.system("clear")
         print('''\033[7;35mQuestão 2\033[m

\033[0;35mQuem descobriu o Brasil?
          
[ \033[m0\033[0;35m ] Santos Dumont
[ \033[m1\033[0;35m ] Philo Farnsworth
[ \033[m2\033[0;35m ] Pedro Álvares Cabral
[ \033[m3\033[0;35m ] Thomas Alva Edison\033[m''')
         Qdob = int(input('>> \033[0;33m'))
         if Qdob == 0:
           print('\033[7;31mVixi, errou :/\033[m')
           time.sleep(1.5)
           os.system("clear")
         elif Qdob == 1:
           print('\033[7;31mVixi, errou :/\033[m')
           time.sleep(1.5)
           os.system("clear")
         elif Qdob == 2:
           os.system("clear")
           print('\033[7;32mAcertou :D\033[m')
           time.sleep(1.5)
           os.system("clear")
           print('''\033[7;35mQuestão 3\033[m

\033[0;35mQuantas cores tem o arco-íris?
          
[ \033[m0\033[0;35m ] 7 Cores
[ \033[m1\033[0;35m ] 5 Cores
[ \033[m2\033[0;35m ] 3 Cores
[ \033[m3\033[0;35m ] 9 Cores\033[m''')
           Qctoai = int(input('>> \033[0;33m'))
           if Qctoai == 2:
             print('\033[7;31mVixi, errou :/\033[m')
             time.sleep(1.5)
             os.system("clear")
           elif Qctoai == 1:
             print('\033[7;31mVixi, errou :/\033[m')
             time.sleep(1.5)
             os.system("clear")
           elif Qctoai == 0:
             os.system("clear")
             print('\033[7;32mAcertou :D\033[m')
             time.sleep(1.5)
             os.system("clear")
             print('''\033[7;35mQuestão 4\033[m
             	
\033[0;35mQual o maior planeta do nosso sistema solar?
             	
[ \033[m0\033[0;35m ] Plutão
[ \033[m1\033[0;35m ] Júpiter
[ \033[m2\033[0;35m ] Saturno
[ \033[m3\033[0;35m ] Marte\033[m''')
             Qompdnss = int(input('>> \033[0;33m'))
             if Qompdnss == 0:
                 print('\033[7;31mVixi, errou :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")
             elif Qompdnss == 1:
                 os.system("clear")
                 print('\033[7;32mAcertou :D\033[m')
                 time.sleep(1.5)
                 os.system("clear")
                 print('''\033[7;35mQuestão 5\033[m
                       
\033[0;35mQual desse animais são carnívoros?
               
[ \033[m0\033[0;35m ] Avestruz
[ \033[m1\033[0;35m ] Elefante
[ \033[m2\033[0;35m ] Crocodilo
[ \033[m3\033[0;35m ] Tigre\033[m''')
                 Qdasc = int(input('>> \033[0;33m'))
                 if Qdasc == 0:
                    print('\033[7;31mVixi, errou :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                 elif Qdasc == 1:
                    print('\033[7;31mVixi, errou :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                 elif Qdasc == 2:
                    print('\033[7;31mVixi, errou :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                 elif Qdasc == 3:
                    os.system("clear")
                    print('\033[7;32mAcertou :D\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                    print('''\033[7;35mQuestão 6\033[m
                       
\033[0;35mO que é comemorado no dia 25/12?
               
[ \033[m0\033[0;35m ] Natal
[ \033[m1\033[0;35m ] Halloween
[ \033[m2\033[0;35m ] Páscoa
[ \033[m3\033[0;35m ] Carnaval\033[m''')
                    Oqecndvd = int(input('>> \033[0;33m'))
                    if Oqecndvd == 0:
                        os.system("clear")
                        print('\033[7;32mAcertou :D\033[m')
                        time.sleep(1.5)
                        os.system("clear")
                        print('''\033[7;35mQuestão 7\033[m

\033[0;35mQual o mês que tem 28 dias?
               
[ \033[m0\033[0;35m ] Janeiro
[ \033[m1\033[0;35m ] Março
[ \033[m2\033[0;35m ] Fevereiro
[ \033[m3\033[0;35m ] Abril\033[m''')
                        Qomqtvod = int(input('>> \033[0;33m'))
                        if Qomqtvod == 0:
                            print('\033[7;31mVixi, errou :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")                 
                        elif Qomqtvod == 1:
                            print('\033[7;31mVixi, errou :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")               
                        elif Qomqtvod == 2:
                            os.system("clear")
                            print ('\033[7;32mAcertou :D\033[m')
                            time.sleep(1.5)
                            os.system("clear")
                            print('''\033[7;35mQuestão 8\033[m
                       
\033[0;35mQuantas letras tem o alfabeto?
     
[ \033[m0\033[0;35m ] 32 Letras
[ \033[m1\033[0;35m ] 22 Letras
[ \033[m2\033[0;35m ] 26 letras
[ \033[m3\033[0;35m ] 27 Letras\033[m''')
                            Qltoa = int(input('>> \033[0;33m'))
                            if Qltoa == 0:
                                print('\033[7;31mVixi, errou :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")
                            elif Qltoa == 1:
                                print('\033[7;31mVixi, errou :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")
                            elif Qltoa == 3:
                                print('\033[7;31mVixi, errou :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                                                                
                            elif Qltoa == 2:
                                os.system("clear")
                                print('\033[7;32mAcertou :D\033[m')
                                time.sleep(1.5)
                                os.system("clear")
                                print('''\033[7;35mQuestão 9\033[m
                       
\033[0;35mQual é o rio mais poluído do mundo?
     
[ \033[m0\033[0;35m ] Rio Hualai
[ \033[m1\033[0;35m ] Rio Tietê
[ \033[m2\033[0;35m ] Rio Amazonas
[ \033[m3\033[0;35m ] Rio Paraná\033[m''')
                                Qeormpdm = int(input('>> \033[0;33m'))
                                if Qeormpdm == 0:
                                    print('\033[7;31mVixi, errou :/\033[m')
                                    time.sleep(1.5)
                                    os.system("clear")
                                elif Qeormpdm == 1:
                                    os.system("clear")
                                    print('\033[7;32mAcertou :D\033[m')
                                    time.sleep(1.5)
                                    os.system("clear")
                                elif Qeormpdm == 2:
                                    print('\033[7;31mVixi, errou :/\033[m')
                                    time.sleep(1.5)
                                    os.system("clear")
                                elif Qeormpdm == 3:
                                    print('\033[7;31mVixi, errou :/\033[m')
                                    time.sleep(1.5)
                                    os.system("clear")
                                else:
                                    print('\033[7;35mOpção inválida. Tente novamente.\033[m')
                                    time.sleep(1)
                                    os.system("clear")
                            else:
                                print('\033[7;35mOpção inválida. Tente novamente.\033[m')
                                time.sleep(1)
                                os.system("clear")

                        elif Qomqtvod == 3:
                            print('\033[7;31mVixi, errou :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")
                        else:
                            print('\033[7;35mOpção inválida. Tente novamente.\033[m')
                            time.sleep(1)
                            os.system("clear")
                                
                    elif Oqecndvd == 1:
                        print('\033[7;31mVixi, errou :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")                
                    elif Oqecndvd == 2:
                        print('\033[7;31mVixi, errou :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")               
                    elif Oqecndvd == 3:
                        print('\033[7;31mVixi, errou :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")                 
                    else:
                        print('\033[7;35mOpção inválida. Tente novamente.\033[m')        
                        time.sleep(1)
                        os.system("clear")
                        
             elif Qompdnss == 2:
                 print('\033[7;31mVixi, errou :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")               
             elif Qompdnss == 3:
                 print('\033[7;31mVixi, errou :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")                 
             else:
                 print('\033[7;35mOpção inválida. Tente novamente.\033[m')
                 time.sleep(1)
                 os.system("clear")
                 
           elif Qctoai == 3:
             print('\033[7;31mVixi, errou :/\033[m')
             time.sleep(1.5)
             os.system("clear")
           else:
             print('\033[7;35mOpção inválida. Tente novamente.\033[m')
             time.sleep(1)
             os.system("clear")
             
         elif Qdob == 3:
           print('\033[7;31mVixi, errou :/\033[m')
           time.sleep(1.5)
           os.system("clear")
         else:
           print('\033[7;35mOpção inválida. Tente novamente.\033[m')
           time.sleep(1)
           os.system("clear")
           
      elif Qfasgm == 1:
          print('\033[7;31mVixi, errou :/\033[m')
          time.sleep(1.5)
          os.system("clear")
      elif Qfasgm == 2:
          print('\033[7;31mVixi, errou :/\033[m')
          time.sleep(1.5)
          os.system("clear")
      elif Qfasgm == 0:
          print('\033[7;31mVixi, errou :/\033[m')
          time.sleep(1.5)
          os.system("clear")
      else:
          print('\033[7;35mOpção inválida. Tente novamente.\033[m')
          time.sleep(1)
          os.system("clear")   
          
   elif opção == 98:
       os.system("clear")
       break
   elif opção == 99:
       print('\033[7;35mVocê saiu do Quiz. Volte sempre!\033[m')
       exit()
          
   else:
       print('\033[7;35mOpção inválida. Tente novamente\033[m')      
       time.sleep(1)
       os.system("clear")
       
 elif Idioma == 1:
  while True:
   print('''\033[0;35m[ \033[m0\033[0;35m ] Start
      
[ \033[m98\033[0;35m ] Language
[ \033[m99\033[0;35m ]\033[m \033[0;31mExit\033[m''')
   opção = int(input('>> \033[0;33m'))
   if opção == 0:
      os.system("clear")
      print('\033[0;35mOk, let`s start\033[m')
      time.sleep(2)
      os.system("clear")
      print('''\033[7;35mQuestion 1\033[m

\033[0;35mWhen was the second world war?
          
[ \033[m0\033[0;35m ] 1914
[ \033[m1\033[0;35m ] 1976
[ \033[m2\033[0;35m ] 1854
[ \033[m3\033[0;35m ] 1939\033[m''')
      Wwtsww = int(input('>> \033[0;33m'))
      if Wwtsww == 3:
         os.system("clear")
         print('''\033[7;32mCorrect :D\033[m''')
         time.sleep(1.5)
         os.system("clear")
         print('''\033[7;35mQuestion 2\033[m

\033[0;35mWho discovered the america?
          
[ \033[m0\033[0;35m ] Santos Dumont
[ \033[m1\033[0;35m ] Philo Farnsworth
[ \033[m2\033[0;35m ] Pedro Christopher Colombia
[ \033[m3\033[0;35m ] Thomas Alva Edison\033[m''')
         Wdta = int(input('>> \033[0;33m'))
         if Wdta == 0:
           print('\033[7;31mUh, wrong :/\033[m')
           time.sleep(1.5)
           os.system("clear")
         elif Wdta == 1:
             print('\033[7;31mUh, wrong :/\033[m')
             time.sleep(1.5)
             os.system("clear")
         elif Wdta == 2:
           os.system("clear")
           print('\033[7;32mCorrect :D\033[m')
           time.sleep(1.5)
           os.system("clear")
           print('''\033[7;35mQuestion 3\033[m

\033[0;35mHow many colors does the rainbow have?
          
[ \033[m0\033[0;35m ] 7 Colors
[ \033[m1\033[0;35m ] 5 Colors
[ \033[m2\033[0;35m ] 3 Colors
[ \033[m3\033[0;35m ] 9 Colors\033[m''')
           Hmcdtrh = int(input('>> \033[0;33m'))
           if Hmcdtrh == 2:
             print('\033[7;31mUh, wrong :/\033[m')
             time.sleep(1.5)
             os.system("clear")
           elif Hmcdtrh == 1:
             print('\033[7;31mUh, wrong :/\033[m')
             time.sleep(1.5)
             os.system("clear")
           elif Hmcdtrh == 0:
             os.system("clear")
             print('\033[7;32mCorrect :D\033[m')
             time.sleep(1.5)
             os.system("clear")
             print('''\033[7;35mQuestion 4\033[m
             	
\033[0;35mWhat is the largest planet in our solar system?
             	
[ \033[m0\033[0;35m ] Pluto
[ \033[m1\033[0;35m ] Jupiter
[ \033[m2\033[0;35m ] Saturn
[ \033[m3\033[0;35m ] Mars\033[m''')
             Witlpioss = int(input('>> \033[0;33m'))
             if Witlpioss == 0:
                 print('\033[7;31mUh, wrong :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")
             elif Witlpioss == 1:
                 os.system("clear")
                 print('\033[7;32mCorrect :D\033[m')
                 time.sleep(1.5)
                 os.system("clear")
                 print('''\033[7;35mQuestion 5\033[m
                       
\033[0;35mWhich of these animals are carnivores?
               
[ \033[m0\033[0;35m ] Ostrich
[ \033[m1\033[0;35m ] Elephant
[ \033[m2\033[0;35m ] Crocodile
[ \033[m3\033[0;35m ] Tiger\033[m''')
                 Wotaac = int(input('>> \033[0;33m'))
                 if Wotaac == 0:
                    print('\033[7;31mUh, wrong :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")                 
                 elif Wotaac == 1:
                    print('\033[7;31mUh, wrong :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")                 
                 elif Wotaac == 2:
                    print('\033[7;31mUh, wrong :/\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                 elif Wotaac == 3:
                    os.system("clear")
                    print('\033[7;32mCorrect :D\033[m')
                    time.sleep(1.5)
                    os.system("clear")
                    print('''\033[7;35mQuestion 6\033[m
                       
\033[0;35mWhat is celebrated on 25/12?
               
[ \033[m0\033[0;35m ] Christmas
[ \033[m1\033[0;35m ] Halloween
[ \033[m2\033[0;35m ] Easter
[ \033[m3\033[0;35m ] Carnival\033[m''')
                    Wicosla = int(input('>> \033[0;33m'))
                    if Wicosla == 0:
                        os.system("clear")
                        print('\033[7;32mCorrect :D\033[m')
                        time.sleep(1.5)
                        os.system("clear")
                        print('''\033[7;35mQuestion 7\033[m

\033[0;35mWhich month has 28 days?
               
[ \033[m0\033[0;35m ] January
[ \033[m1\033[0;35m ] March
[ \033[m2\033[0;35m ] February
[ \033[m3\033[0;35m ] April\033[m''')
                        Wmhslad = int(input('>> \033[0;33m'))
                        if Wmhslad == 0:
                            print('\033[7;31mUh, wrong :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")                        
                        elif Wmhslad == 1:
                            print('\033[7;31mUh, wrong :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")
                        elif Wmhslad == 2:
                            os.system("clear")
                            print('\033[7;32mCorrect :D\033[m')
                            time.sleep(1.5)
                            os.system("clear")
                            print('''\033[7;35mQuestion 8\033[m
                       
\033[0;35mHow many letters does the alphabet have?
     
[ \033[m0\033[0;35m ] 32 Letters
[ \033[m1\033[0;35m ] 22 Letters
[ \033[m2\033[0;35m ] 26 Letters
[ \033[m3\033[0;35m ] 27 Letters\033[m''')
                            Hmldtah = int(input('>> \033[0;33m'))
                            if Hmldtah == 0:
                                print('\033[7;31mUh, wrong :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                
                            elif Hmldtah == 1:
                                print('\033[7;31mUh, wrong :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                 
                            elif Hmldtah == 3:
                                print('\033[7;31mUh, wrong :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                
                            elif Hmldtah == 2:
                                os.system("clear")
                                print('\033[7;32mCorrect :D\033[m')
                                time.sleep(1.5)
                                os.system("clear")
                                print('''\033[7;35mQuestion 9\033[m
                                
\033[0;35mWhat is the most polluted river in the world?
     
[ \033[m0\033[0;35m ] Hualai River
[ \033[m1\033[0;35m ] Tiete River
[ \033[m2\033[0;35m ] Amazon river
[ \033[m3\033[0;35m ] Parana River\033[m''')
                            Witmpritw = int(input('>> \033[0;33m'))
                            if Witmpritw == 0:
                                print('\033[7;31mUh, wrong :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                
                            elif Witmpritw == 1:
                                os.system("clear")
                                print('\033[7;32mCorrect :D\033[m')
                                time.sleep(1.5)
                                os.system("clear")
                            elif Witmpritw == 2:
                                print('\033[7;31mUh, wrong :/\033[m')
                                time.sleep(1.5)
                                os.system("clear")                
                            elif Witmpritw == 3:
                                print('\033[7;31muh, wrong :/\033[m')          
                                time.sleep(1.5)
                                os.system("clear")                
                            else:
                                print('\033[7;35mInvalid option. Try again.\033[m') 
                                time.sleep(1) 
                                os.system("clear")
                                  
                        elif Wmhslad == 3:
                            print('\033[7;31mUh, wrong :/\033[m')
                            time.sleep(1.5)
                            os.system("clear")                
                        else:
                            print('\033[7;35mInvalid option. Try again.\033[m')
                            time.sleep(1)
                            os.system("clear")  
             

                    elif Wicosla == 1:
                        print('\033[7;31mUh, wrong :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")                
                    elif Wicosla == 2:
                        print('\033[7;31mUh, wrong :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")                
                    elif Wicosla == 3:
                        print('\033[7;31mUh, wrong :/\033[m')
                        time.sleep(1.5)
                        os.system("clear")                
                    else:
                        print('\033[7;35mInvalid option. Try again.\033[m')
                        time.sleep(1)
                        os.system("clear") 
                 else:
                      print('\033[7;35mInvalid option. Try again.\033[m')
                      time.sleep(1)
                      os.system("clear")              
             
             elif Witlpioss == 2:
                 print('\033[7;31mUh, wrong :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")                
             elif Witlpioss == 3:
                 print('\033[7;31mUh, wrong :/\033[m')
                 time.sleep(1.5)
                 os.system("clear")                
             else:
                 print('\033[7;35mInvalid option. Try again.\033[m')
                 time.sleep(1)
                 os.system("clear")  
                  
           elif Hmcdtrh == 3:
             print('\033[7;31mUh, wrong :/\033[m')
             time.sleep(1.5)
             os.system("clear")                
           else:              
             print('\033[7;35mInvalid option. Try again.\033[m')
             time.sleep(1)
             os.system("clear")  
             
         elif Wdta == 3:
           print('\033[7;31mUh, wrong :/\033[m')
           time.sleep(1.5)
           os.system("clear")               
         else:
             print('\033[7;35mInvalid option. Try again.\033[m')
             time.sleep(1)
             os.system("clear")  
                      
      elif Wwtsww == 1:
          print('\033[7;31mUh, wrong :/\033[m')
          time.sleep(1.5)
          os.system("clear")                
      elif Wwtsww == 2:
          print('\033[7;31mUh, wrong :/\033[m')
          time.sleep(1.5)
          os.system("clear")                
      elif Wwtsww == 0:
          print('\033[7;31mUh, wrong :/\033[m')
          time.sleep(1.5)
          os.system("clear")                
      else:
          print('\033[7;35mInvalid option. Try again.\033[m')
          time.sleep(1)
          os.system("clear")
               
   elif opção == 98:
       os.system("clear")
       break
   elif opção == 99:
       print('\033[7;35mYou left the Quiz. Come back anytime!\033[m')
       exit()
          
   else:
       print('\033[7;35mInvalid option. Try again.\033[m')      
       time.sleep(1)
       os.system("clear")
 else:
    print('\033[7;35mOpção inválida. | Invalid option.\033[m')  
    time.sleep(1)
    os.system("clear")  
