import sys, os, pika
import tkinter as tk
import tkinter.ttk as ttk
from Usuario import Usuarios
from threading import Thread
import threading

class Application(tk.Tk):
    def __init__(self):
        '''This class configures and populates the rootlevel window.
           root is the rootlevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        tk.Tk.__init__(self)
        self.geometry("800x600+388+129")
        self.title("Concord")
        self.configure(background="#363636")
        self.menubar  = tk.Menu(self,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.15, rely=0.2, relheight=0.592, relwidth=0.7)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#292929")

        self.user = tk.Entry(self.Frame1)
        self.user.place(relx=0.161, rely=0.31, height=30, relwidth=0.596)
        self.user.configure(background="white")
        self.user.configure(disabledforeground="#a3a3a3")
        self.user.configure(font="TkFixedFont")
        self.user.configure(foreground="#000000")
        self.user.configure(insertbackground="black")

        self.lbuser = tk.Label(self.Frame1)
        self.lbuser.place(relx=0.089, rely=0.225, height=18, width=216)
        self.lbuser.configure(background="#292929")
        self.lbuser.configure(disabledforeground="#a3a3a3")
        self.lbuser.configure(font="-family {Reem Kufi} -size 14")
        self.lbuser.configure(foreground="#9d9d9d")
        self.lbuser.configure(justify='left')
        self.lbuser.configure(text='''Nome de Usuário''')

        self.lbpass = tk.Label(self.Frame1)
        self.lbpass.place(relx=0.054, rely=0.423, height=18, width=173)
        self.lbpass.configure(activebackground="#f9f9f9")
        self.lbpass.configure(activeforeground="black")
        self.lbpass.configure(background="#292929")
        self.lbpass.configure(disabledforeground="#a3a3a3")
        self.lbpass.configure(font="-family {Reem Kufi} -size 14")
        self.lbpass.configure(foreground="#9d9d9d")
        self.lbpass.configure(highlightbackground="#d9d9d9")
        self.lbpass.configure(highlightcolor="black")
        self.lbpass.configure(justify='left')
        self.lbpass.configure(text='''Senha''')

        self.password = tk.Entry(self.Frame1, show='*')
        self.password.place(relx=0.161, rely=0.507, height=30, relwidth=0.596)
        self.password.configure(background="white")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(font="TkFixedFont")
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(insertbackground="black")
        self.password.configure(selectbackground="blue")
        self.password.configure(selectforeground="white")

        self.btlogin = tk.Button(self.Frame1, command=self.logarUsuario)
        self.btlogin.place(relx=0.161, rely=0.676, height=44, width=334)
        self.btlogin.configure(activebackground="#778fce")
        self.btlogin.configure(activeforeground="#040404")
        self.btlogin.configure(background="#4161b4")
        self.btlogin.configure(cursor="tcross")
        self.btlogin.configure(disabledforeground="#a3a3a3")
        self.btlogin.configure(font="-family {Reem Kufi} -size 15")
        self.btlogin.configure(foreground="#ffffff")
        self.btlogin.configure(highlightbackground="#778fce")
        self.btlogin.configure(highlightcolor="#778fce")
        self.btlogin.configure(overrelief="flat")
        self.btlogin.configure(pady="0")
        self.btlogin.configure(relief="flat")
        self.btlogin.configure(text='''Entrar''')

        self.lbpass_1 = tk.Label(self.Frame1)
        self.lbpass_1.place(relx=0.161, rely=0.817, height=18, width=148)
        self.lbpass_1.configure(activebackground="#f9f9f9")
        self.lbpass_1.configure(activeforeground="black")
        self.lbpass_1.configure(background="#292929")
        self.lbpass_1.configure(disabledforeground="#a3a3a3")
        self.lbpass_1.configure(font="-family {Reem Kufi} -size 9")
        self.lbpass_1.configure(foreground="#535353")
        self.lbpass_1.configure(highlightbackground="#d9d9d9")
        self.lbpass_1.configure(highlightcolor="black")
        self.lbpass_1.configure(justify='left')
        self.lbpass_1.configure(text='''Precisando de uma conta?''')

        self.btregister = tk.Button(self.Frame1, command=self.cadastro)
        self.btregister.place(relx=0.429, rely=0.817, height=18, width=69)
        self.btregister.configure(activebackground="#778fce")
        self.btregister.configure(activeforeground="#000000")
        self.btregister.configure(background="#292929")
        self.btregister.configure(cursor="tcross")
        self.btregister.configure(disabledforeground="#a3a3a3")
        self.btregister.configure(font="-family {Reem Kufi} -size 9")
        self.btregister.configure(foreground="#4161b4")
        self.btregister.configure(highlightbackground="#778fce")
        self.btregister.configure(highlightcolor="#778fce")
        self.btregister.configure(overrelief="flat")
        self.btregister.configure(pady="0")
        self.btregister.configure(relief="flat")
        self.btregister.configure(text='''Registre-se''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.286, rely=0.056, height=41, width=194)
        self.Label1.configure(background="#292929")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Reem Kufi} -size 20")
        self.Label1.configure(foreground="#9d9d9d")
        self.Label1.configure(text='''Bem-vindo!''')

    def registrarUsuario(self):
        user = Usuarios()
        users = user.selectAllUsers()
        user.usuario = self.registeruser.get()
        user.senha = self.registerpassword.get()

        for usuarios in users:
            if usuarios[1] == user.usuario:
                if usuarios[2] == user.senha:
                    self.Label1["text"] = "Usuário já cadastrado."
                    break
                else:
                    continue
            else:
                continue
        else:
            if "".__eq__(user.usuario):
                if "".__eq__(user.senha):
                   self.Label1["text"] = "Um ou mais campos estão vazios."
                   return
            self.Label1["text"] = user.insertUser()
            self.registeruser.delete(0, tk.END)
            self.registerpassword.delete(0, tk.END)
            self.destroy()

    def logarUsuario(self):
        user = Usuarios()
        users = user.selectAllUsers()
        usuario = self.user.get()
        senha = self.password.get()

        for usuarios in users:
            if usuarios[1] == usuario:
                if usuarios[2] == senha:
                    self.destroy()
                    rabbitMQ(usuario).mainloop()
                    

                else:
                    continue
            else:
                continue    

    def cadastro(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        cadastro = tk.Toplevel(self)
        cadastro.geometry("800x600+388+129")
        cadastro.title("Cadastro")
        cadastro.configure(background="#363636")
        cadastro.configure(highlightbackground="#d9d9d9")
        cadastro.configure(highlightcolor="black")

        self.menubar = tk.Menu(cadastro,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        cadastro.configure(menu = self.menubar)

        self.FrameCadastro = tk.Frame(cadastro)
        self.FrameCadastro.place(relx=0.15, rely=0.2, relheight=0.592, relwidth=0.7)
        self.FrameCadastro.configure(relief='flat')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(background="#292929")
        self.FrameCadastro.configure(highlightbackground="#d9d9d9")
        self.FrameCadastro.configure(highlightcolor="black")

        self.registeruser = tk.Entry(self.FrameCadastro)
        self.registeruser.place(relx=0.161, rely=0.31, height=30, relwidth=0.596)
        self.registeruser.configure(background="white")
        self.registeruser.configure(disabledforeground="#a3a3a3")
        self.registeruser.configure(font="TkFixedFont")
        self.registeruser.configure(foreground="#000000")
        self.registeruser.configure(highlightbackground="#d9d9d9")
        self.registeruser.configure(highlightcolor="black")
        self.registeruser.configure(insertbackground="black")
        self.registeruser.configure(selectbackground="blue")
        self.registeruser.configure(selectforeground="white")

        self.lbuser = tk.Label(self.FrameCadastro)
        self.lbuser.place(relx=0.089, rely=0.225, height=18, width=216)
        self.lbuser.configure(background="#292929")
        self.lbuser.configure(disabledforeground="#a3a3a3")
        self.lbuser.configure(font="-family {Reem Kufi} -size 14")
        self.lbuser.configure(foreground="#9d9d9d")
        self.lbuser.configure(highlightbackground="#d9d9d9")
        self.lbuser.configure(highlightcolor="black")
        self.lbuser.configure(justify='left')
        self.lbuser.configure(text='''Nome de Usuário''')

        self.lbpass = tk.Label(self.FrameCadastro)
        self.lbpass.place(relx=0.054, rely=0.423, height=18, width=173)
        self.lbpass.configure(activebackground="#f9f9f9")
        self.lbpass.configure(activeforeground="black")
        self.lbpass.configure(background="#292929")
        self.lbpass.configure(disabledforeground="#a3a3a3")
        self.lbpass.configure(font="-family {Reem Kufi} -size 14")
        self.lbpass.configure(foreground="#9d9d9d")
        self.lbpass.configure(highlightbackground="#d9d9d9")
        self.lbpass.configure(highlightcolor="black")
        self.lbpass.configure(justify='left')
        self.lbpass.configure(text='''Senha''')

        self.registerpassword = tk.Entry(self.FrameCadastro)
        self.registerpassword.place(relx=0.161, rely=0.507, height=30, relwidth=0.596)
        self.registerpassword.configure(background="white")
        self.registerpassword.configure(disabledforeground="#a3a3a3")
        self.registerpassword.configure(font="TkFixedFont")
        self.registerpassword.configure(foreground="#000000")
        self.registerpassword.configure(highlightbackground="#d9d9d9")
        self.registerpassword.configure(highlightcolor="black")
        self.registerpassword.configure(insertbackground="black")
        self.registerpassword.configure(selectbackground="blue")
        self.registerpassword.configure(selectforeground="white")

        self.btregister = tk.Button(self.FrameCadastro, command=self.registrarUsuario)
        self.btregister.place(relx=0.161, rely=0.676, height=44, width=334)
        self.btregister.configure(activebackground="#778fce")
        self.btregister.configure(activeforeground="#040404")
        self.btregister.configure(background="#4161b4")
        self.btregister.configure(cursor="tcross")
        self.btregister.configure(disabledforeground="#a3a3a3")
        self.btregister.configure(font="-family {Reem Kufi} -size 15")
        self.btregister.configure(foreground="#ffffff")
        self.btregister.configure(highlightbackground="#778fce")
        self.btregister.configure(highlightcolor="#778fce")
        self.btregister.configure(overrelief="flat")
        self.btregister.configure(pady="0")
        self.btregister.configure(relief="flat")
        self.btregister.configure(text='''Cadastrar''')

        self.Label1 = tk.Label(self.FrameCadastro)
        self.Label1.place(relx=0.0, rely=0.056, height=41, width=564)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#292929")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Reem Kufi} -size 20")
        self.Label1.configure(foreground="#9d9d9d")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Cadastre-se!''')


class rabbitMQ(tk.Tk):
    def __init__(self, usuario):
        '''This class configures and populates the self.rootlevel window.
           self.root is the self.rootlevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        tk.Tk.__init__(self)
        strvar = tk.StringVar()
        strvar.set("Nada foi enviado.")
        self.geometry("1024x768+296+119")
        self.minsize(120, 1)
        self.maxsize(1684, 1031)
        self.resizable(1,  1)
        self.title("RabbitMQ")
        self.configure(background="#707070")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")
        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.113, rely=0.117, relheight=0.788, relwidth=0.764)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#595959")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")


        self.lbname = tk.Label(self.Frame1)
        self.lbname.place(relx=0.016, rely=0.042, height=30, width=173)
        self.lbname.configure(activebackground="#f9f9f9")
        self.lbname.configure(activeforeground="black")
        self.lbname.configure(anchor='sw')
        self.lbname.configure(background="#595959")
        self.lbname.configure(disabledforeground="#a3a3a3")
        self.lbname.configure(font="-family {Reem Kufi} -size 12")
        self.lbname.configure(foreground="#ffffff")
        self.lbname.configure(highlightbackground="#d9d9d9")
        self.lbname.configure(highlightcolor="black")
        var = "Bem-vindo,  {fname}".format(fname=usuario)
        self.usuario = usuario
        self.lbname.configure(text=var)
        self.listUsers = tk.Listbox(self.Frame1)
        self.listUsers.place(relx=0.051, rely=0.215, relheight=0.331
                , relwidth=0.312)
        self.listUsers.configure(background="#0c0c21")
        self.listUsers.configure(disabledforeground="#a3a3a3")
        self.listUsers.configure(font="-family {Reem Kufi} -size 10")
        self.listUsers.configure(foreground="#ffffff")
        self.listUsers.configure(highlightbackground="#d9d9d9")
        self.listUsers.configure(highlightcolor="#6c6c6c")
        self.listUsers.configure(relief="flat")
        self.listUsers.configure(selectbackground="#c0c0c0")
        self.listUsers.configure(selectforeground="white")
        user = Usuarios()
        users = user.selectAllUsers()
        i = 1
        for usuarios in users:
           # if(usuarios[1] == usuario):
            #    continue
            #else:
                self.listUsers.insert(i, usuarios[1])
                i+=1
        self.receptor = {"nome": 'usuario'}
        def selectUser(event):
            index = self.listUsers.curselection()
            self.receptor = self.listUsers.get(index)
        self.listUsers.bind('<ButtonRelease-1>', selectUser)

        self.showmessages = tk.Label(self.Frame1, text="Aguardando...")
        self.showmessages.place(relx=0.448, rely=0.05, relheight=0.745, relwidth=0.507)
        self.showmessages.configure(background="#d9d9d9")
        self.showmessages.configure(font="-family {Reem Kufi} -size 10")
        self.showmessages.configure(foreground="#000000")
        self.showmessages.configure(highlightbackground="#d9d9d9")
        self.showmessages.configure(highlightcolor="black")
        self.showmessages.configure(width=310)

        self.listGroup = tk.Listbox(self.Frame1)
        self.listGroup.place(relx=0.051, rely=0.645, relheight=0.331, relwidth=0.312)
        self.listGroup.configure(background="#0c0c21")
        self.listGroup.configure(disabledforeground="#a3a3a3")
        self.listGroup.configure(font="-family {Reem Kufi} -size 10")
        self.listGroup.configure(foreground="#ffffff")
        self.listGroup.configure(highlightbackground="#d9d9d9")
        self.listGroup.configure(highlightcolor="#c8c8c8")
        self.listGroup.configure(relief="flat")
        self.listGroup.configure(selectbackground="#c0c0c0")
        self.listGroup.configure(selectforeground="white")
        self.listGroup.insert(1, "Público")

        def selectGroup(event):
            index = self.listGroup.curselection()
            self.receptor =  self.listGroup.get(index)
        self.listGroup.bind('<ButtonRelease-1>', selectGroup)

        self.typing = tk.Entry(self.Frame1)
        self.typing.place(relx=0.448, rely=0.826, height=40, relwidth=0.384)
        self.typing.configure(background="white")
        self.typing.configure(disabledforeground="#a3a3a3")
        self.typing.configure(font="TkFixedFont")
        self.typing.configure(foreground="#000000")
        self.typing.configure(highlightbackground="#d9d9d9")
        self.typing.configure(highlightcolor="black")
        self.typing.configure(insertbackground="black")
        self.typing.configure(selectbackground="blue")
        self.typing.configure(selectforeground="white")

        self.btEnviar = tk.Button(self.Frame1, command=self.enviarMensagem)
        self.btEnviar.place(relx=0.871, rely=0.826, height=40, width=67)
        self.btEnviar.configure(activebackground="#ececec")
        self.btEnviar.configure(activeforeground="#000000")
        self.btEnviar.configure(background="#d9d9d9")
        self.btEnviar.configure(cursor="fleur")
        self.btEnviar.configure(disabledforeground="#a3a3a3")
        self.btEnviar.configure(foreground="#000000")
        self.btEnviar.configure(highlightbackground="#d9d9d9")
        self.btEnviar.configure(highlightcolor="black")
        self.btEnviar.configure(pady="0")
        self.btEnviar.configure(text='''Enviar''')

        self.lbuserguide = tk.Label(self.Frame1)
        self.lbuserguide.place(relx=0.141, rely=0.165, height=21, width=95)
        self.lbuserguide.configure(background="#595959")
        self.lbuserguide.configure(disabledforeground="#a3a3a3")
        self.lbuserguide.configure(font="-family {Reem Kufi} -size 14")
        self.lbuserguide.configure(foreground="#ffffff")
        self.lbuserguide.configure(text='''Usuários''')

        self.lbgroupguide = tk.Label(self.Frame1)
        self.lbgroupguide.place(relx=0.141, rely=0.595, height=21, width=96)
        self.lbgroupguide.configure(activebackground="#f9f9f9")
        self.lbgroupguide.configure(activeforeground="black")
        self.lbgroupguide.configure(background="#595959")
        self.lbgroupguide.configure(disabledforeground="#a3a3a3")
        self.lbgroupguide.configure(font="-family {Reem Kufi} -size 14")
        self.lbgroupguide.configure(foreground="#ffffff")
        self.lbgroupguide.configure(highlightbackground="#d9d9d9")
        self.lbgroupguide.configure(highlightcolor="black")
        self.lbgroupguide.configure(text='''Grupos''')

        td = Receptores(usuario, self)
        tr = ReceptoresFanOut(usuario, self)
        td.start()
        tr.start()      


    def enviarMensagem(self):
        params = pika.URLParameters('amqps://cjcdhnkl:9V5CEDFSyjDsCyMNeYRoPsYs6Zh30KHJ@jackal.rmq.cloudamqp.com/cjcdhnkl')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        mensagem = self.usuario
        if(self.receptor == "Público"):
            channel.exchange_declare(exchange=self.receptor, exchange_type='fanout')
            mensagem = mensagem + " (Público): " + self.typing.get()
            channel.basic_publish(exchange=self.receptor, routing_key='', body=mensagem)
            print(" [x] Enviado para o Grupo %r" % mensagem)
            connection.close()
        else:     
            channel.queue_declare(queue=self.receptor, durable=True)
            mensagem = mensagem + ": " + self.typing.get()
            mensagem.encode('utf-8')
            channel.basic_publish(exchange='', routing_key=self.receptor, body=mensagem, properties=pika.BasicProperties(
                            delivery_mode = 2,))
            print(' [x] Mensagem Enviada!')
            connection.close()
        self.typing.delete(0, tk.END)   
        return 

    def receberMensagem(self, body):
        aux = self.showmessages["text"]
        var = ("%r" % body.decode('utf-8'))
        textinho =  aux + "\n" + var
        self.showmessages['text'] = textinho
    def receberFanOut(self, body):
        aux = self.showmessages["text"]
        var = ("%r" % body.decode('utf-8'))
        textinho =  aux + "\n" + var
        self.showmessages.config(text = textinho)
        self.showmessages['text'] = textinho
        print(self.showmessages['text'])

class Receptores(threading.Thread):
    def __init__(self, user, parent):
        Thread.__init__(self)
        self.user = user
        self.parent = parent
    def callback(self, ch, method, properties, body):
        print(" [x] Mensagem recebida %r" % body.decode('utf-8'))
        rm = self.parent
        rm.receberMensagem(body) 

    def run(self):
        params = pika.URLParameters('amqps://cjcdhnkl:9V5CEDFSyjDsCyMNeYRoPsYs6Zh30KHJ@jackal.rmq.cloudamqp.com/cjcdhnkl')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_consume(queue=self.user, on_message_callback=self.callback, auto_ack=True)
        print(' [*] Aguardando mensagens')
        channel.start_consuming()

class ReceptoresFanOut(threading.Thread):
    def __init__(self, user, parent):
        Thread.__init__(self)
        self.user = user
        self.parent = parent

    def run(self):
        params = pika.URLParameters('amqps://cjcdhnkl:9V5CEDFSyjDsCyMNeYRoPsYs6Zh30KHJ@jackal.rmq.cloudamqp.com/cjcdhnkl')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.exchange_declare(exchange='Público', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='Público', queue=queue_name)

        def callback(ch, method, properties, body):
            print(" [x] Mensagem recebida no Grupo Público: %r" % body)
            rm = self.parent
            rm.receberFanOut(body) 
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print(' [*] Aguardando mensagens')
        channel.start_consuming()


app = Application()
app.mainloop()