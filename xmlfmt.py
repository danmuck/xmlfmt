#!/usr/bin/python

# basic [in progress] XML formatter in Python3 + BASH 
# *maybe works with Powershell on Windows

import os, platform

P_NAME = str
      
def p_start():
    cmd_start = input('\n\n [f] if starting with a new project or [?] for more options. \n\n:')
    if cmd_start == '':
        p_start()
    elif cmd_start == 'f':
        global P_NAME
        P_NAME = input('Project Name:\n').replace(' ', '_')
        app_file(f'  :: {P_NAME} :: \n\n<xml>')
        app_menu()
    elif cmd_start == '?':
        print(''' 

    XMLil-Help
        enter: #
            f: initialize new [project_name].xml
            e: menu for current [project_name].xml
            w: end xml file
            r: change active [project_name].xml
            k: kill current project (rm -rf project_name.xml)
            q: exit

                ''')
        p_start()

    elif cmd_start == 'e':
        if os.path.exists(f'./xml_projects/{P_NAME}.xml'):
            app_menu()
        else:
            print('Not currently working on a project...')
            p_start()

    elif cmd_start == 'w':
        app_file('</xml>\n\n')
        P_NAME = input('\nNew project name: ').replace(' ', '_')
        p_start()

    elif cmd_start == 'k':
        def kill_script():
            if (platform.system) == 'Windows':
                print('Error: killscript() not compatible with Windows at this time')
            else:
                os.system(f'rm -rf ./xml_projects/{P_NAME}.xml')
        kill_script()
        p_start()

    elif cmd_start == 'r':
        P_NAME = input('\nNew project name: ').replace(' ', '_')
        app_menu()

    elif cmd_start == 'q':
        return exit

    elif cmd_start == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        pre_cat()
        print('\n\n')
        p_start()

    else:
        p_start()

def app_menu():
    m_opt = input('\n\n [c]new_class\n [a]new_activity\n [f]new_xmlblock\n [p]preview\n [q]back\n\n:')
    if m_opt == 'c':
        xml_class()

    elif m_opt == 'f':
        app_file(f'\n\n<xml>')
        xml_class()

    elif m_opt == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        pre_cat()
        print('\n\n')  
        app_menu()

    elif m_opt == 'q':
        p_start()

    else:
        app_menu()

#CLASSES
def xml_class():
    c_name = input('\nPlease enter a name for a class\n\n:')
    app_file(f'\t<class>\n\t\t<name>{c_name}</name>')
    c_prompt()

def c_prompt(): 
    choice = input('Class | \n| [1]inherits [2]property(b) [3]property(n/t) [4]method(b) [5]method(o)\n| [f]new [w]end [p]pr [?]help\n\n:')

    if choice == '?':
        print('\n\n [1]inheritance\n [2]property(basic)\n [3]property(name/type)\n [4]method(basic)\n [5]method(options)\n [f]newclass\n [w]endclass \n [p]preview \n [q]exit\n\n')
        c_prompt()

    elif choice == 'f':
        xml_class()

    elif choice == 'w':
        app_file(f'\t</class>')
        c_prompt()

    elif choice == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        pre_cat()
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
    a_opt = input('\nMethod |\n [1]parameter\n [2]return statement\n [w]endmethod \n\n:')
    if a_opt == '1':
        app_file(f'\t\t\t<parameter>')
        def m_params():
            m_param = input('\nParameter |\n [1]name\n [2]type\n [w]endparam \n\n:')
            if m_param == '1':
                param_name = input('Name: ')
                app_file(f'\t\t\t\t<name>{param_name}</name>')
                m_params()
            elif m_param == '2':
                param_type = input('Type: ')
                app_file(f'\t\t\t\t<type>{param_type}</type>')
                m_params()
            elif m_param == 'w':
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

    elif a_opt == 'w':
        app_file(f'\t\t</method>')
        c_prompt()
    
    else:
        m_add()

#ACTIVITIES
def xml_activity():
    a_name = input('\nPlease enter a name for an activity\n\n:')
    app_file(f'\t<activity>\n\t\t<name>{a_name}</name>')
    ac_prompt()

def ac_prompt(): 
    choice = input('Activity | \n| [1]statement [2]selection [3] [4] [5]\n| [f]new [w]end [p]pr [?]help\n\n:')

    if choice == '?':
        print('\n\n [1]\n [2]\n [3]\n [4]\n [5]\n [f]newactivity\n [w]endactivity \n [p]preview \n [q]exit\n\n')
        ac_prompt()

    elif choice == 'f':
        xml_activity()

    elif choice == 'w':
        app_file(f'\t</activity>')
        ac_prompt()

    elif choice == 'p':
        print(f'Preview of {P_NAME}.xml:\n\n')
        pre_cat()
        print('\n\n')
        ac_prompt()

    elif choice == '1':
        inh_name = input('Inherits: ')
        app_file(f'\t\t<inherits>{inh_name}</inherits>')
        ac_prompt()

    elif choice == '2':
        pb_name = input('Property Name: ')
        app_file(f'\t\t<property>\n\t\t\t<name>{pb_name}</name>\n\t\t</property>')
        ac_prompt()

    elif choice == '3':
        p_name = input('Property Name: ')
        p_type = input('Property Type: ')
        app_file(f'\t\t<property>\n\t\t\t<name>{p_name}</name>\n\t\t\t<type>{p_type}</type>\n\t\t</property>')
        ac_prompt()

    elif choice == '4':
        mb_name = input('Method name: ')
        app_file(f'\t\t<method>\n\t\t\t<name>{mb_name}</name>\n\t\t</method>')
        ac_prompt()

    elif choice == '5':
        m_name = input('Method name: ')
        app_file(f'\t\t<method>\n\t\t\t<name>{m_name}</name>')
        m_add()
    
    elif choice == 'q':
        p_start()

    else:
        ac_prompt()

#RUN

def mk_dir():
    if platform.system() == 'Windows':
        if not os.path.exists('.\\xml_projects'):
            os.system(f'mkdir xml_projects')
            print('Saving files to .\\xml_projects')
        else:
            print('Saving files to .\\xml_projects')
    elif not os.path.exists('./xml_projects'):
        os.system(f'mkdir xml_projects')
        print('Saving files to ./xml_projects')
    else:
        print('Saving files to ./xml_projects')

def app_file(ctx):
    lin_dir = f'./xml_projects/{P_NAME}.xml'
    win_dir = f'.\\xml_projects\\{P_NAME}.xml'
    if platform.system() == 'Windows':
        with open(f'{win_dir}', 'a') as f:
            f.write(f'{str(ctx)}\n')
        with open(f'{win_dir}', 'r') as o:
            print('\n\n' + o.read())
    else:
        with open(f'{lin_dir}', 'a') as f:
            f.write(f'{str(ctx)}\n')
        with open(f'{lin_dir}', 'r') as o:
            print('\n\n' + o.read())
   
def pre_cat():
    if platform.system() == 'Windows':
        with open(f'.\\xml_projects\\{P_NAME}.xml', 'r') as o:
            print('\n\n' + o.read())        
    else:
        with open(f'./xml_projects/{P_NAME}.xml', 'r') as o:
            print('\n\n' + o.read())
  
print('\n\n :: Welcome to XMLfmt :: \n')
mk_dir()
p_start()


