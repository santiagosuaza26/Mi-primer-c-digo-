import tkinter as tk
from tkinter import messagebox,Frame, ttk
from datetime import datetime



def abrir_interfaz_tareas():
    menu_principal.destroy()  # Cerrar la ventana de menú principal
    crear_interfaz_tareas()   # Abrir la interfaz de tareas

def abrir_gestor_notas():
    menu_principal.destroy()
    crear_interfaz_notas()

def abrir_gestor_eventos():
    menu_principal.destroy()
    abrir_interfaz_eventos()

def crear_interfaz_notas():

    notas = []

    # Funciones
    def agregar_nota():
        titulo = titulo_entry.get()
        contenido = contenido_entry.get("1.0", tk.END).strip()
        if titulo and contenido:
            fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notas.append({'Titulo': titulo, 'Contenido': contenido, 'Fecha de Creación': fecha_creacion})
            actualizar_listbox()
            messagebox.showinfo("Nota agregada", "Nota agregada correctamente")
            limpiar_campos()
        else:
            messagebox.showerror("Error", "Complete todos los campos")

    def limpiar_campos():
        titulo_entry.delete(0, tk.END)
        contenido_entry.delete("1.0", tk.END)

    def actualizar_listbox():
        listbox.delete(0, tk.END)
        for nota in sorted(notas, key=lambda x: x['Fecha de Creación'], reverse=True):
            listbox.insert(tk.END, nota['Titulo'])

    def mostrar_contenido_seleccionado(event):
        selected_index = listbox.curselection()
        if selected_index:
            nota_seleccionada = notas[selected_index[0]]
            titulo_entry.delete(0, tk.END)
            titulo_entry.insert(tk.END, nota_seleccionada['Titulo'])
            contenido_entry.delete("1.0", tk.END)
            contenido_entry.insert(tk.END, nota_seleccionada['Contenido'])

    def buscar_notas():
        texto_busqueda = buscar_entry.get().lower()
        if texto_busqueda:
            notas_encontradas = [nota for nota in notas if texto_busqueda in nota['Titulo'].lower() or texto_busqueda in nota['Contenido'].lower()]
            listbox.delete(0, tk.END)
            for nota in notas_encontradas:
                listbox.insert(tk.END, nota['Titulo'])
        else:
            actualizar_listbox()

    def eliminar_nota():
        selected_index = listbox.curselection()
        if selected_index:
            nota_eliminada = notas.pop(selected_index[0])
            messagebox.showinfo("Nota eliminada", f"Nota '{nota_eliminada['Titulo']}' eliminada correctamente")
            limpiar_campos()
            actualizar_listbox()

    def editar_nota():
        selected_index = listbox.curselection()
        if selected_index:
            nota_seleccionada = notas[selected_index[0]]
            titulo = titulo_entry.get()
            contenido = contenido_entry.get("1.0", tk.END).strip()
            if titulo and contenido:
                nota_seleccionada['Titulo'] = titulo
                nota_seleccionada['Contenido'] = contenido
                messagebox.showinfo("Nota editada", "Nota editada correctamente")
                limpiar_campos()
                actualizar_listbox()
            else:
                messagebox.showerror("Error", "Complete todos los campos")

    # Creación de la ventana principal
    app = tk.Tk()
    app.title("Gestor de Notas")
    app.geometry("500x450")

    # Definir el marco
    marco_principal = tk.Frame(app)
    marco_principal.pack(padx=10, pady=10)

    # Crear Listbox
    listbox = tk.Listbox(marco_principal)
    listbox.pack(side=tk.LEFT, padx=10, pady=10)
    listbox.bind("<<ListboxSelect>>", mostrar_contenido_seleccionado)

    # Campos de entrada y botones
    marco_campos = tk.Frame(marco_principal)
    marco_campos.pack(side=tk.LEFT, padx=10, pady=10)

    tk.Label(marco_campos, text="Título: ").grid(row=0, column=0, sticky="w")
    titulo_entry = tk.Entry(marco_campos)
    titulo_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(marco_campos, text="Contenido: ").grid(row=1, column=0, sticky="w")
    contenido_entry = tk.Text(marco_campos, height=6, width=25)
    contenido_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(marco_campos, text="Agregar Nota", command=agregar_nota).grid(row=2, column=0, columnspan=2, pady=5)
    tk.Button(marco_campos, text="Eliminar Nota", command=eliminar_nota).grid(row=3, column=0, columnspan=2, pady=5)
    tk.Button(marco_campos, text="Editar Nota", command=editar_nota).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(marco_campos, text="VOLVER AL MENU", command=mostrar_menu_principal).grid(row=4, column=3, padx=5)
    # Barra de búsqueda
    buscar_label = tk.Label(app, text="Buscador")
    buscar_label.pack(padx=10, pady=5)
    buscar_entry = tk.Entry(app)
    buscar_entry.pack(fill=tk.X, padx=10, pady=5)
    buscar_entry.bind('<KeyRelease>', lambda event: buscar_notas())

    # Inicializar la lista
    actualizar_listbox()

    app.mainloop()


def crear_interfaz_tareas():
    #lista
    tareas = []


    #Funciones de menu
    def agregar_tarea():
        titulo = titulo_entry.get()
        descripcion = descripcion_entry.get()
        fecha_v = fecha_entry.get()
        prioridad = prioridad_entry.get()
        if titulo and descripcion and fecha_v and prioridad:
            tareas.append({'Titulo': titulo, 'Descripcion': descripcion, 'Fecha': fecha_v, 'Prioridad': prioridad, 'Completa': False})
            actualizar_listbox()
            messagebox.showinfo("Tarea agregada", "Tarea agregada completa")
            limpiar_campos()
        else:
            messagebox.showerror("Complete todos los campos")


    def mostrar_tareas():
        if not tareas:
            messagebox.showinfo("No hay tareas pendientes")
        else:
            tareas_pendientes = "\n".join([f"{i+1}, {tarea['Titulo']} - Fecha de vencimiento:{tarea['Fecha']} - Prioridad: {tarea['Prioridad']}" for i, tarea in enumerate(tareas) if not tarea['Completa']])
            messagebox.showinfo("Tareas pendientes", tareas_pendientes)


    def limpiar_campos():
        titulo_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
        fecha_entry.delete(0, tk.END)
        prioridad_entry.delete(0, tk.END)

    def marcar_completada():
        selected_index = listbox.curselection()
        if selected_index:
            tareas.pop(selected_index[0])
            # Actualizar la Listbox
            actualizar_listbox()
        messagebox.showinfo("Tarea Completada","Tarea Mela")

    def editar_tarea():
        selected_index = listbox.curselection()
        if selected_index:
            tarea_seleccionada = tareas[selected_index[0]]
            # Llenar campos de entrada con la información de la tarea seleccionada
            titulo_entry.delete(0, tk.END)
            titulo_entry.insert(tk.END, tarea_seleccionada['Titulo'])
            descripcion_entry.delete(0, tk.END)
            descripcion_entry.insert(tk.END, tarea_seleccionada['Descripcion'])
            fecha_entry.delete(0, tk.END)
            fecha_entry.insert(tk.END, tarea_seleccionada['Fecha'])
            prioridad_entry.delete(0, tk.END)
            prioridad_entry.insert(tk.END, tarea_seleccionada['Prioridad'])

            # Botón para guardar cambios
            guardar_button = tk.Button(botones_frame, text="Guardar Cambios", command=lambda: guardar_cambios(selected_index[0]))
            guardar_button.grid(row=0, column=3, padx=5)

    def guardar_cambios(index):
        titulo = titulo_entry.get()
        descripcion = descripcion_entry.get()
        fecha_v = fecha_entry.get()
        prioridad = prioridad_entry.get()
        if titulo and descripcion and fecha_v and prioridad:
            tareas[index]['Titulo'] = titulo
            tareas[index]['Descripcion'] = descripcion
            tareas[index]['Fecha'] = fecha_v
            tareas[index]['Prioridad'] = prioridad
            actualizar_listbox()
            messagebox.showinfo("Tarea Editada", "Los cambios se han guardado correctamente")
        else:
            messagebox.showerror("Complete todos los campos")


    def actualizar_listbox():
        # Borrar todas las tareas actuales
        listbox.delete(0, tk.END)
        # Agregar las tareas actualizadas
        for tarea in tareas:
            listbox.insert(tk.END, tarea['Titulo'])


    # Creación de la ventana principal
    app = tk.Tk()
    app.title("Agenda personal de Leonardo")
    app.geometry("500x450")

    #frame1 
    frame1=  Frame(app, bg="#F3DCDB")
    frame1.pack(expand=True , fill='both')


    # Crear Listbox
    listbox = tk.Listbox(frame1)
    listbox.pack(padx=15, pady=15 )

    # Agregar tareas a la Listbox
    for tarea in tareas:
        listbox.insert(tk.END, tarea['Titulo'])


    # Botón para eliminar tarea
    eliminar_button = tk.Button(frame1, text="Marcar como completada", command=marcar_completada)
    eliminar_button.pack()
    #Definir el marco
    input_frame = tk.Frame(frame1, bg= "#F3DCDB")
    input_frame.pack(before=listbox ,padx=10, pady=10)

    #Campos de entrada
    tk.Label(input_frame, text="Titulo: ").grid(row=0, column=0, sticky="w")
    titulo_entry = tk.Entry(input_frame)
    titulo_entry.grid(row=0, column= 1, padx=5, pady=5)

    tk.Label(input_frame, text="Descripcion: ").grid(row=1, column=0, sticky="w")
    descripcion_entry = tk.Entry(input_frame)
    descripcion_entry.grid(row=1, column= 1, padx=5, pady=5)

    tk.Label(input_frame, text="Fecha de vencimiento [DD/MM/AAAA]: ").grid(row=2, column=0, sticky="w")
    fecha_entry = tk.Entry(input_frame)
    fecha_entry.grid(row=2, column= 1, padx=5, pady=5)

    tk.Label(input_frame, text="Prioridad: ").grid(row=3, column=0, sticky="w")
    prioridad_entry = tk.Entry(input_frame)
    prioridad_entry.grid(row=3, column= 1, padx=5, pady=5)  

    #Botones|   

    botones_frame = tk.Frame(frame1)
    botones_frame.pack(padx=10, pady=10)

    tk.Button(botones_frame, text="Agregar Tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
    tk.Button(botones_frame, text="Mostrar Tareas Pendientes", command=mostrar_tareas).grid(row=0, column=1, padx=5)
    tk.Button(botones_frame, text="Editar Tarea", command=editar_tarea).grid(row=0, column=2, padx=5)
    tk.Button(botones_frame, text="VOLVER AL MENU", command=mostrar_menu_principal).grid(row=4, column=3, padx=5)
    #Variable tareas completas

    tarea_seleccionada_var = tk.StringVar()
    tarea_seleccionada_var.set('')



    app.mainloop()

def abrir_interfaz_eventos():

    # Estructura de datos para almacenar eventos
    eventos = []

    # Funciones de Registro de Eventos
    def agregar_evento():
        # Obtener datos del formulario
        titulo = titulo_entry.get()
        descripcion = descripcion_entry.get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        ubicacion = ubicacion_entry.get()

        # Validar que se hayan ingresado todos los datos
        if titulo and descripcion and fecha and hora and ubicacion:
            # Agregar evento a la lista de eventos
            eventos.append({'Titulo': titulo, 'Descripcion': descripcion, 'Fecha': fecha, 'Hora': hora, 'Ubicacion': ubicacion})
            messagebox.showinfo("Evento Agregado", "El evento se ha agregado correctamente.")
            limpiar_campos()
            actualizar_listbox()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def limpiar_campos():
        titulo_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
        fecha_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)
        ubicacion_entry.delete(0, tk.END)

    def actualizar_listbox():
        eventos_listbox.delete(0, tk.END)
        for evento in eventos:
            eventos_listbox.insert(tk.END, evento['Titulo'])

    # Funciones de Consulta de Eventos
    def mostrar_eventos():
        # Mostrar una lista de todos los eventos próximos
        if eventos:
            eventos_ordenados = sorted(eventos, key=lambda x: (x['Fecha'], x['Hora']))
            lista_eventos = "\n".join([f"{evento['Titulo']} - {evento['Fecha']} - {evento['Hora']} - {evento['Ubicacion']}" for evento in eventos_ordenados])
            messagebox.showinfo("Eventos Próximos", lista_eventos)
        else:
            messagebox.showinfo("Eventos Próximos", "No hay eventos programados.")  

    def filtrar_eventos():
    # Permitir al usuario filtrar los eventos por fecha, hora o tipo
        def filtrar():
            opcion = filtro_var.get()

            if opcion == "Fecha":
                fecha = fecha_filtro_entry.get()
                eventos_filtrados = [evento for evento in eventos if evento['Fecha'] == fecha]
                mostrar_resultados(eventos_filtrados)

            elif opcion == "Hora":
                hora = hora_filtro_entry.get()
                eventos_filtrados = [evento for evento in eventos if evento['Hora'] == hora]
                mostrar_resultados(eventos_filtrados)

            elif opcion == "Tipo":
                tipo = ()
                eventos_filtrados = [evento for evento in eventos if evento['Tipo'] == tipo]
                mostrar_resultados(eventos_filtrados)

            else:
                messagebox.showerror("Error", "Seleccione una opción de filtro válida.")

        def actualizar_campos_filtro(*args):
            opcion = filtro_var.get()

            if opcion == "Fecha":
                fecha_filtro_entry.config(state="normal")
                hora_filtro_entry.config(state="disabled")

            elif opcion == "Hora":
                fecha_filtro_entry.config(state="disabled")
                hora_filtro_entry.config(state="normal")
                
        def mostrar_resultados(eventos_filtrados):
            if eventos_filtrados:
                lista_filtrada = "\n".join([f"{evento['Titulo']} - {evento['Fecha']} - {evento['Hora']} - {evento['Ubicacion']}" for evento in eventos_filtrados])
                messagebox.showinfo("Eventos Filtrados", lista_filtrada)
            else:
                messagebox.showinfo("Eventos Filtrados", "No se encontraron eventos que coincidan con los criterios de filtrado.")



        # Crear ventana emergente para el filtro
        ventana_filtro = tk.Toplevel(app)
        ventana_filtro.title("Filtrar Eventos")
        ventana_filtro.geometry("300x200")

        filtro_var = tk.StringVar(ventana_filtro)
        filtro_var.set("Tipo")  # Opción predeterminada
        filtro_var.trace("w", actualizar_campos_filtro)  # Vincular la actualización de campos a la opción seleccionada

        tk.Label(ventana_filtro, text="Seleccione el tipo de filtro:").pack(pady=5)

        filtro_option_menu = tk.OptionMenu(ventana_filtro, filtro_var, "Fecha", "Hora", "Tipo")
        filtro_option_menu.pack(pady=5)

        tk.Label(ventana_filtro, text="Fecha (DD/MM/AAAA):").pack(pady=5)
        fecha_filtro_entry = tk.Entry(ventana_filtro, state="disabled")
        fecha_filtro_entry.pack(pady=5)

        tk.Label(ventana_filtro, text="Hora (HH:MM): ").pack(pady=5)
        hora_filtro_entry = tk.Entry(ventana_filtro, state="disabled")
        hora_filtro_entry.pack(pady=5)


        tk.Button(ventana_filtro, text="Filtrar", command=filtrar).pack(pady=5)


    def buscar_eventos():
        # Permitir al usuario buscar eventos por título o descripción
        def buscar():
            termino_busqueda = termino_busqueda_entry.get().lower()
            eventos_encontrados = [evento for evento in eventos if termino_busqueda in evento['Titulo'].lower() or termino_busqueda in evento['Descripcion'].lower()]
            mostrar_resultados(eventos_encontrados)

        def mostrar_resultados(eventos_encontrados):
            if eventos_encontrados:
                lista_encontrados = "\n".join([f"{evento['Titulo']} - {evento['Fecha']} - {evento['Hora']} - {evento['Ubicacion']}" for evento in eventos_encontrados])
                messagebox.showinfo("Eventos Encontrados", lista_encontrados)
            else:
                messagebox.showinfo("Eventos Encontrados", "No se encontraron eventos que coincidan con el término de búsqueda.")

        # Crear ventana emergente para la búsqueda
        ventana_busqueda = tk.Toplevel(app)
        ventana_busqueda.title("Buscar Eventos")
        ventana_busqueda.geometry("300x150")

        tk.Label(ventana_busqueda, text="Buscar por título o descripción:").pack(pady=5)

        termino_busqueda_entry = tk.Entry(ventana_busqueda)
        termino_busqueda_entry.pack(pady=5)

        tk.Button(ventana_busqueda, text="Buscar", command=buscar).pack(pady=5)


    # Funciones de Gestión de Eventos
    def editar_evento():
        # Editar un evento existente
        def guardar_cambios():
            index = eventos_listbox.curselection()
            if index:
                evento_seleccionado = eventos[index[0]]
                evento_seleccionado['Titulo'] = titulo_edit_entry.get()
                evento_seleccionado['Descripcion'] = descripcion_edit_entry.get()
                evento_seleccionado['Fecha'] = fecha_edit_entry.get()
                evento_seleccionado['Hora'] = hora_edit_entry.get()
                evento_seleccionado['Ubicacion'] = ubicacion_edit_entry.get()
                messagebox.showinfo("Evento Editado", "Los cambios se han guardado correctamente.")
                actualizar_listbox()
            else:
                messagebox.showerror("Error", "Seleccione un evento para editarlo.")

        def seleccionar_evento(event):
            index = eventos_listbox.curselection()
            if index:
                evento_seleccionado = eventos[index[0]]
                titulo_edit_entry.delete(0, tk.END)
                titulo_edit_entry.insert(tk.END, evento_seleccionado['Titulo'])
                descripcion_edit_entry.delete(0, tk.END)
                descripcion_edit_entry.insert(tk.END, evento_seleccionado['Descripcion'])
                fecha_edit_entry.delete(0, tk.END)
                fecha_edit_entry.insert(tk.END, evento_seleccionado['Fecha'])
                hora_edit_entry.delete(0, tk.END)
                hora_edit_entry.insert(tk.END, evento_seleccionado['Hora'])
                ubicacion_edit_entry.delete(0, tk.END)
                ubicacion_edit_entry.insert(tk.END, evento_seleccionado['Ubicacion'])

        # Crear ventana emergente para la edición
        ventana_edicion = tk.Toplevel(app)
        ventana_edicion.title("Editar Evento")
        ventana_edicion.geometry("400x250")

        eventos_listbox = tk.Listbox(ventana_edicion)
        eventos_listbox.pack(padx=10, pady=10)
        eventos_listbox.bind('<<ListboxSelect>>', seleccionar_evento)

        for evento in eventos:
            eventos_listbox.insert(tk.END, evento['Titulo'])

        tk.Label(ventana_edicion, text="Título:").pack(pady=5)
        titulo_edit_entry = tk.Entry(ventana_edicion)
        titulo_edit_entry.pack(pady=5)

        tk.Label(ventana_edicion, text="Descripción:").pack(pady=5)
        descripcion_edit_entry = tk.Entry(ventana_edicion)
        descripcion_edit_entry.pack(pady=5)

        tk.Label(ventana_edicion, text="Fecha:").pack(pady=5)
        fecha_edit_entry = tk.Entry(ventana_edicion)
        fecha_edit_entry.pack(pady=5)

        tk.Label(ventana_edicion, text="Hora:").pack(pady=5)
        hora_edit_entry = tk.Entry(ventana_edicion)
        hora_edit_entry.pack(pady=5)

        tk.Label(ventana_edicion, text="Ubicación:").pack(pady=5)
        ubicacion_edit_entry = tk.Entry(ventana_edicion)
        ubicacion_edit_entry.pack(pady=5)

        tk.Button(ventana_edicion, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)

    def eliminar_evento():
        selected_index = eventos_listbox.curselection()
        if selected_index:
            eventos.pop(selected_index[0])
            # Actualizar la Listbox
            actualizar_listbox()
        messagebox.showinfo("Eliminar","Eliminado con exito.")

    # Crear la ventana principal
    app = tk.Tk()
    app.title("Gestor de Eventos")
    app.geometry("500x500")

    # Interfaz de Registro de Eventos
    # Campos de entrada
    tk.Label(app, text="Título:").grid(row=0, column=0, sticky="w")
    titulo_entry = tk.Entry(app)
    titulo_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(app, text="Descripción:").grid(row=1, column=0, sticky="w")
    descripcion_entry = tk.Entry(app)
    descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(app, text="Fecha:").grid(row=2, column=0, sticky="w")
    fecha_entry = tk.Entry(app)
    fecha_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(app, text="Hora:").grid(row=3, column=0, sticky="w")
    hora_entry = tk.Entry(app)
    hora_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(app, text="Ubicación:").grid(row=4, column=0, sticky="w")
    ubicacion_entry = tk.Entry(app)
    ubicacion_entry.grid(row=4, column=1, padx=5, pady=5)

    # ListBox para mostrar eventos
    eventos_listbox = tk.Listbox(app)
    eventos_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    # Botones
    tk.Button(app, text="Agregar Evento", command=agregar_evento).grid(row=5, column=0, columnspan=2, pady=10)
    tk.Button(app, text="Mostrar Eventos", command=mostrar_eventos).grid(row=7, column=0, pady=5)
    tk.Button(app, text="Filtrar Eventos", command=filtrar_eventos).grid(row=7, column=1, pady=5)
    tk.Button(app, text="Buscar Eventos", command=buscar_eventos).grid(row=8, column=0, pady=5)
    tk.Button(app, text="Editar Evento", command=editar_evento).grid(row=8, column=1, pady=5)
    tk.Button(app, text="Eliminar Evento", command=eliminar_evento).grid(row=8, column=2, pady=5)
    tk.Button(app, text="VOLVER AL MENU", command=mostrar_menu_principal).grid(row=4, column=3, padx=5)

def mostrar_menu_principal():
    # Crear la ventana del menú principal
    global menu_principal  # Declarar la ventana como global para poder cerrarla más tarde
    menu_principal = tk.Tk()
    menu_principal.title("Menú Principal")
    menu_principal.geometry("300x200")

    # Etiqueta de bienvenida
    tk.Label(menu_principal, text="Bienvenido al Sistema", font=("Arial", 13)).pack(pady=20)

    # Botones de opciones
    tk.Button(menu_principal, text="Administrar Tareas", command=abrir_interfaz_tareas).pack(pady=10)
    tk.Button(menu_principal, text="Administrar Notas", command=abrir_gestor_notas).pack(pady=10)
    tk.Button(menu_principal, text="Administrar Eventos", command=abrir_gestor_eventos).pack(pady=10)
    # Ejecutar el bucle principal
    menu_principal.mainloop()

# Llamar a la función para mostrar el menú principal
mostrar_menu_principal()
