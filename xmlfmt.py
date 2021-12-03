#!/usr/bin/python3

# basic XML formatter in Python3 + BASH 
# *maybe works with Powershell on Windows

import os

P_NAME = str

def p_start():
    cmd_start = input('\n\n [f] if starting with a new project or [?] for more options. \n\n:')
    if cmd_start == '':
        p_start()
    elif cmd_start == 'f':
        global P_NAME
        P_NAME = input('Project Name:\n')
        app_file(f'  :: {P_NAME} :: \n\n<xml>')
        nc_check()
    elif cmd_start == '?':
        print(''' 

    XMLil-Help
        enter: #
            f: initialize new [project_name].xml
            w: end xml file
            r: replace [project_name]
            k: kill current file (rm -rf project_name.xml)
            q: exit

                ''')
        p_start()

    elif cmd_start == 'w':
        app_file('</xml>\n\n\n\n\n\t\t created with XMLfmt :) \n\n\n\n\n')
        P_NAME = input('\nNew project name: ')
        p_start()

    elif cmd_start == 'k':
        def kill_script():
            #posix
            os.system(f'rm -rf ./xml_projects/{P_NAME}.xml')
        kill_script()
        p_start()

    elif cmd_start == 'r':
        P_NAME = input('\nNew project name: ')
        nc_check()

    elif cmd_start =='q':
        return exit

    elif cmd_start =='p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        os.system(f'cat ./xml_projects/{P_NAME}.xml')
        print('\n\n')
        p_start()

    else:
        p_start()

def nc_check():
    n_c = input('\n\n [c]new_class\n [a]new_activity\n [f]new_xmlblock\n [p]preview\n [q]back\n\n:')
    if n_c == 'c':
        xml_class()

    elif n_c == 'f':
        app_file(f'\n\n<xml>')
        xml_class()

    elif n_c == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        os.system(f'cat ./xml_projects/{P_NAME}.xml')
        print('\n\n')  
        nc_check()

    elif n_c == 'q':
        p_start()

    else:
        nc_check()

#CLASSES
def xml_class():
    c_name = input('\nPlease enter a name for a class\n\n:')
    app_file(f'\t<class>\n\t\t<name>{c_name}</name>')
    c_prompt()

def c_prompt(): 
    choice = input('\n[1]i [2]pb [3]p [4]mb [5]m [f]nc [w]ec [p]pr [?]help\n\n:')

    if choice == '?':
        print('\nAdd \n [1]inheritance\n [2]property(basic)\n [3]property(name/type)\n [4]method(basic)\n [5]method(options)\n [f]newclass\n [w]endclass \n [p]preview \n [q]exit')
        c_prompt()

    elif choice == 'f':
        xml_class()

    elif choice == 'w':
        app_file(f'\t</class>')
        c_prompt()

    elif choice == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        os.system(f'cat ./xml_projects/{P_NAME}.xml')
        print('\n\n')
        c_prompt()

    elif choice == '1':
        inh_name = input('Inherits: ')
        app_file(f'\t\t<inherits>{inh_name}</inherits>')
        c_prompt()

    elif choice == '2':
        pb_name = input('Property Name: ')
        app_file(f'\t\t<property>\n\t\t\t<name>{pb_name}</name>\n\t\t</property>')
        c_prompt()

    elif choice == '3':
        p_name = input('Property Name: ')
        p_type = input('Property Type: ')
        app_file(f'\t\t<property>\n\t\t\t<name>{p_name}</name>\n\t\t\t<type>{p_type}</type>\n\t\t</property>')
        c_prompt()


    elif choice == '4':
        mb_name = input('Method name: ')
        app_file(f'\t\t<method>\n\t\t\t<name>{mb_name}</name>\n\t\t</method>')
        c_prompt()

    elif choice == '5':
        m_name = input('Method name: ')
        app_file(f'\t\t<method>\n\t\t\t<name>{m_name}</name>')
        m_add()
    
    elif choice == 'q':
        p_start()

    else:
        c_prompt()

#METHOD OPTIONS
def m_add():
    a_opt = input('\nAdd \n [1]parameter\n [2]return\n [3]endmethod \n\n:')
    if a_opt == '1':
        app_file(f'\t\t\t<parameter>')
        def m_params():
            m_param = input('\n [1]name\n [2]type\n [3]endparam \n\n:')
            if m_param == '1':
                param_name = input('Name: ')
                app_file(f'\t\t\t\t<name>{param_name}</name>')
                m_params()
            elif m_param == '2':
                param_type = input('Type: ')
                app_file(f'\t\t\t\t<type>{param_type}</type>')
                m_params()
            elif m_param == '3':
                app_file(f'\t\t\t</parameter>')
                m_add()
            else:
                m_params()
        m_params()

    elif a_opt == '2':
        def m_returns():
            m_return = input('Returns: ')
            app_file(f'\t\t\t<returns>{m_return}</returns>')
            m_add()
        m_returns()

    elif a_opt == '3':
        app_file(f'\t\t</method>')
        c_prompt()
    
    else:
        m_add()

#ACTIVITIES
def xml_activity():
    a_name = input('\nPlease enter a name for an activity\n\n:')
    app_file(f'\t<activity>\n\t\t<name>{a_name}</name>')
    c_prompt()

#RUN
print('\n\n :: Welcome to XMLfmt :: \n')
os.system('./xtra.sh')

def app_file(ctx):
    lin_dir = f'./xml_projects/{P_NAME}.xml'
    win_dir = f'.\\xml_projects\\{P_NAME}.xml'
    if (os.name) == 'nt':
        os.system(f"echo '{str(ctx)}' >> {win_dir}")
    else:
        os.system(f"echo '{str(ctx)}' >> {lin_dir}")
   
p_start()