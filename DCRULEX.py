Skip to content

t3am21

/

DC

Public

Code

Issues

Pull requests

Actions

Projects

Wiki

Security

Insights

dcrulex786/DCRULEX.py

@dcrulex786

dcrulex786 Update DCRULEX.py

 1 contributor

 55 lines (39 sloc)  1.52 KB

 import mechanize

 import facebook

 import time

# Browser

br = mechanize.Browser()

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

print ("[+] TH3 DC RUL3X [+]")

print ("[+] by Dc Boyz [+]")

msg=str(input("Enter your Token : "))

poct=str(input("Enter your post Link : "))

token=msg

def auto_post():

 while True:

     graph = facebook.GraphAPI(access_token=token,version='2.8')

    graph.put_object(parent_object= poct, connection_name='comments',message='#DC_RUL3X_H3R3')

        print ("Comment Done!\n")

            time.sleep(200)

    graph.put_object(parent_object=poct, connection_name='comments',message='#DC_RUL3X_0N_F1R3')

        print ("Comment Done!\n")

            time.sleep(200)

                graph.put_object(parent_object=poct, connection_name='comments',message='#DC_RUL3X_4KK4_KH0F_XD')

                    print ("Comment Done!\n")

                        time.sleep(200)

                            graph.put_object(parent_object=poct, connection_name='comments',message='#DC_RUL3X_0N_T4B4H1')

                                print ("Comment Done!\n")

                                    time.sleep(200)

if __name__ == '__main__':

    auto_post()

        print ("Comment Done!\n")

        #Code agar copy krte ho to nam hata shakte ho

        © 2022 GitHub, Inc.

        Terms

        Privacy

        Security

        Status

        Docs

        Contact GitHub

        Pricing

        API

        Training

        Blog

        About

        Loading complete
