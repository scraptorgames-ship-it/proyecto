import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from db import consultar, ejecutar
from logic import (BG, WHITE, NAVY, BLUE, MUTED, BORDER, PALE, GREEN, RED, YELLOW,
                   fecha_hoy, fecha_valida)

class PanelMixin:
    def estilizar(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Treeview", background=WHITE, fieldbackground=WHITE,
                        foreground=NAVY, rowheight=29, bordercolor=BORDER,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#76B7ED", foreground=NAVY,
                        font=("Segoe UI", 10, "bold"), relief="flat")
        style.map("Treeview", background=[("selected", "#58CCE3")], foreground=[("selected", NAVY)])
        
        style.configure("TCombobox", padding=5)
        style.configure("TNotebook", background=BG, borderwidth=0)
        style.configure("TNotebook.Tab", padding=(12, 8), font=("Segoe UI", 10, "bold"))
    def limpiar(self):
        for w in self.root.winfo_children():
            w.destroy()
    def boton(self, parent, texto, comando, principal=False):
        return tk.Button(parent, text=texto, command=comando,
                         bg="#0B3550" if principal else "#E5F2F8",
                         fg=WHITE if principal else "#19324D",
                         activebackground="#4BADF3" if principal else "#4BADF3",
                         activeforeground=WHITE if principal else NAVY,
                         relief="flat", bd=0, cursor="hand2",
                         font=("Segoe UI", 11, "bold"), padx=13, pady=8,width="30",
                         highlightthickness=0)
    def mostrar_login(self):
        self.limpiar()
        shell = tk.Frame(self.root, bg=WHITE)
        shell.place(x=0, y=0, relwidth=1, relheight=1)
        brand = tk.Frame(shell, bg=NAVY, width=700)
        brand.pack(side="left", fill="y")
        brand.pack_propagate(False)
        tk.Label(brand, text="NZ", bg="#254A64", fg="#A7E3DF", width=2, height=1,
                 font=("Impact", 42, "bold"),highlightbackground="#3C7187",highlightthickness=1).pack(anchor="center", padx=52, pady=(85, 24))
        
        
        tk.Label(brand, text="NEZAHUALCÓYOTL🦢", bg=NAVY, fg="#F8FBFA",
                 font=("Impact", 53, "bold"), ).pack(anchor="center", padx=53)
        tk.Label(brand, text="ESCUELA PRIMARIA", bg=NAVY, fg="#A7E3DF",
                         font=("Segoe UI", 18,"bold")).pack(anchor="center", padx=53)
        tk.Label(brand, text="CONTROL ESCOLAR", bg=NAVY, fg="#F9FFFF",
                 font=("Segoe UI", 12, "bold")).pack(anchor="center", padx=54, pady=(8, 30))
        tk.Frame(brand, bg="#69C6E8", height=4, width=800).pack(anchor="center", padx=53, pady=(0, 24))
        tk.Label(brand, text="Asistencia, seguimiento",
                 bg=NAVY, fg="#F0F5FA", font=("Segoe UI", 15),
                 justify="left").pack(anchor="center", padx=54)
        tk.Label(brand, text="y gestión escolar.",
                         bg=NAVY, fg="#F0F5FA", font=("Segoe UI", 15),
                         justify="left").pack(anchor="center", padx=54)
        tk.Label(brand, text="Acceso para dirección y docentes",
                 bg=NAVY, fg="#C6D8E8", font=("Segoe UI", 10),
                 wraplength=310).pack(side="bottom", anchor="center", padx=54, pady=38)

        right = tk.Frame(shell, bg=WHITE)
        right.pack(side="left", fill="both", expand=True)
        form = tk.Frame(right, bg=WHITE, width=500)
        form.place(relx=.5, rely=.5, anchor="center", relwidth=.72)
        tk.Label(form, text="PRIMARIA NEZAHUALCÓYOTL  /  CONTROL ESCOLAR",
                         bg=WHITE, fg=MUTED, font=("Segoe UI", 15, "bold")).pack(anchor="center", pady=(10, 30))
        tk.Label(form, text="¡Qué gusto verte, Bienvenido!👋🏻", bg=WHITE, fg=NAVY,
                 font=("Impact", 30, "bold")).pack(anchor="w")
       
        tk.Label(form, text="Inicia sesión para continuar",
                 bg=WHITE, fg="#00171F", font=("Segoe UI", 20, "bold")).pack(anchor="center", pady=(15, 30))
        tk.Label(form, text="Ingresa Tu Nombre De Usuario:", bg=WHITE, fg="#2A827C",
                 font=("Impact", 20, "bold")).pack(anchor="center")
        self.login_usuario = tk.Entry(form, font=("Segoe UI", 14,"bold"), relief="solid",
                                      bd=2, width="33", highlightthickness=2,bg="#254A64",fg="#F6F7F7", highlightbackground=BORDER)
        self.login_usuario.pack(ipady=5, pady=(15, 30))
        tk.Label(form, text="Ingresa Tu Contraseña:", bg=WHITE, fg="#2A827C",
                 font=("Impact", 20, "bold")).pack(anchor="center")
        self.login_password = tk.Entry(form, show="*",bg="#254A64",fg="#F6F7F7",font=("Segoe UI", 14),
                                       relief="solid", bd=2,width="37", highlightthickness=2, highlightbackground=BORDER)
        self.login_password.pack(ipady=5, pady=(15, 30))
        tk.Label(form, text="",
                                 bg=WHITE, fg=MUTED, font=("Segoe UI", 15, "bold")).pack(anchor="center", pady=(10, 5))
        self.boton(form, "Iniciar sesión", self.iniciar_sesion, True).pack()
        tk.Label(form, text="",
                 bg=WHITE, fg=MUTED, font=("Segoe UI", 15)).pack(anchor="w", pady=(15, 0))
        self.login_password.bind("<Return>", lambda e: self.iniciar_sesion())
        self.login_usuario.focus_set()
    def mostrar_panel(self):
        self.limpiar()
        top = tk.Frame(self.root, bg=NAVY, height=66)
        top.pack(fill="x")
        top.pack_propagate(False)
        tk.Label(top, text="PRIMARIA NEZAHUALCÓYOTL  |  CONTROL ESCOLAR",
                 bg=NAVY, fg=WHITE, font=("Segoe UI", 13, "bold")).pack(side="left", padx=22)
        tk.Label(top, text=f"{self.usuario['nombre']}  ·  {self.usuario['rol'].title()}",
                 bg=NAVY, fg="#D5E5F1", font=("Segoe UI", 10)).pack(side="right", padx=12)
        self.boton(top, "Cerrar sesión", self.cerrar_sesion).pack(side="right", padx=15, pady=13)
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=18, pady=16)
        if self.usuario["rol"] == "docente":
            self.panel_docente(body)
        elif self.usuario["rol"] == "director":
            self.panel_director(body)
        else:
            tk.Label(body, text="Perfil de tutor: consulta de información escolar.",
                     bg=BG, fg=NAVY, font=("Segoe UI", 16, "bold")).pack(anchor="w")
            tk.Label(body, text="La vista de tutor se puede ampliar cuando se definan sus funciones.",
                     bg=BG, fg=MUTED).pack(anchor="w", pady=8)
    def panel_docente(self, parent):
        grupo = self.grupo_docente()
        if not grupo:
            tk.Label(parent, text="Dirección debe asignarte un grupo antes de registrar asistencia.",
                     bg=BG, fg="#A33", font=("Segoe UI", 11)).pack(anchor="w")
            return
        shell = tk.Frame(parent, bg=BG)
        shell.pack(fill="both", expand=True)
        side = tk.Frame(shell, bg=NAVY, width=305)
        side.pack(side="left", fill="y", padx=(0,14))
        side.pack_propagate(False)
        tk.Label(side, text="MENÚ DOCENTE", bg=NAVY, fg="#B8E6F6",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=18, pady=(22,8))
        tk.Label(side, text=grupo['nombre'], bg=NAVY, fg=WHITE,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=18, pady=(0,22))
        content = tk.Frame(shell, bg=BG)
        content.pack(side="left", fill="both", expand=True)
        def mostrar(vista):
            for w in content.winfo_children(): w.destroy()
            if vista == "asistencia": self.vista_asistencia(content, grupo)
            elif vista == "justificantes": self.vista_justificantes(content, grupo)
            else: self.vista_conducta(content, grupo)
        for texto, vista in [("Pasar lista", "asistencia"), ("Justificantes", "justificantes"), ("Conducta e incidencias", "conducta")]:
            self.boton(side, texto, lambda v=vista: mostrar(v), vista == "asistencia").pack(fill="x", padx=15, pady=5)
        mostrar("asistencia")
    def vista_asistencia(self, parent, grupo):
        bar = tk.Frame(parent, bg=BG)
        bar.pack(fill="x", pady=8)
        tk.Label(bar, text="Fecha", bg=BG, fg=NAVY).pack(side="left")
        fecha_var = tk.StringVar(value=fecha_hoy())
        tk.Entry(bar, textvariable=fecha_var, width=13, font=("Segoe UI", 10),bg="#254A64",fg="#F6F7F7",).pack(side="left", padx=8)
        self.boton(bar, "Cargar lista", lambda: cargar()).pack(side="left", padx=4)
        self.boton(bar, "Todos presentes", lambda: todos_presentes()).pack(side="left", padx=4)
        self.boton(bar, "Guardar asistencia", lambda: guardar(), True).pack(side="right", padx=4)

        columns = ("numero", "nombre", "estado", "justificado", "nota")
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=17, selectmode="browse")
        for col, title, width in [
            ("numero", "N.º", 55), ("nombre", "Alumno", 360), ("estado", "Estado", 125),
            ("justificado", "Justificante", 110), ("nota", "Nota del justificante", 270)
        ]:
            tree.heading(col, text=title)
            tree.column(col, width=width, anchor="w" if col in ("nombre","nota") else "center")
        tree.pack(fill="both", expand=True, pady=6)
        tree.tag_configure("presente", background="#8DEBAC")
        tree.tag_configure("falta", background="#E13C3C")
        tree.tag_configure("retardo", background="#E5B444")
        tk.Label(parent, text="Selecciona un alumno y usa los botones para cambiar su estado.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w")
        controls = tk.Frame(parent, bg=BG)
        controls.pack(fill="x", pady=8)
        self.boton(controls, "✓ Presente", lambda: cambiar_estado("Presente"), True).pack(side="left", padx=(0,6))
        self.boton(controls, "✕ Falta", lambda: cambiar_estado("Falta"), True).pack(side="left", padx=6)
        self.boton(controls, "◷ Retardo", lambda: cambiar_estado("Retardo"), True).pack(side="left", padx=6)
        self.boton(controls, "Registrar justificante", lambda: justificar()).pack(side="left", padx=6)

        alumnos = []
        estados = {}

        def cargar():
            fecha = fecha_var.get().strip()
            if not fecha_valida(fecha):
                messagebox.showwarning("Fecha inválida", "Escribe una fecha válida con año, mes y día (ejemplo: 2026-10-28).")
                return
            try:
                alumnos[:] = consultar("SELECT id, numero_lista, nombre FROM alumnos "
                                       "WHERE grupo_id=%s AND activo=1 ORDER BY numero_lista", (grupo["id"],))
                existentes = consultar("SELECT alumno_id, estado, justificado, nota_justificante "
                                       "FROM asistencias WHERE grupo_id=%s AND fecha=%s",
                                       (grupo["id"], fecha))
                guardados = {r["alumno_id"]: r for r in existentes}
                estados.clear()
                for a in alumnos:
                    r = guardados.get(a["id"])
                    estados[a["id"]] = {
                        "estado": r["estado"] if r else "Presente",
                        "justificado": bool(r["justificado"]) if r else False,
                        "nota": r["nota_justificante"] or "" if r else ""
                    }
                refrescar()
            except Exception as exc:
                messagebox.showerror("Error", str(exc))

        def refrescar():
            tree.delete(*tree.get_children())
            for a in alumnos:
                st = estados[a["id"]]
                tag = st["estado"].lower()
                just = "Sí" if st["justificado"] else "No"
                tree.insert("", "end", iid=str(a["id"]),
                            values=(a["numero_lista"], a["nombre"], st["estado"], just, st["nota"]),
                            tags=(tag,))
        def seleccionado():
            sel = tree.selection()
            if not sel:
                messagebox.showinfo("Selecciona un alumno", "Primero selecciona un alumno de la lista.")
                return None
            return int(sel[0])
        def cambiar_estado(estado):
            aid = seleccionado()
            if aid is None: return
            estados[aid]["estado"] = estado
            if estado == "Presente":
                estados[aid]["justificado"] = False
                estados[aid]["nota"] = ""
            refrescar()
            tree.selection_set(str(aid))
        def todos_presentes():
            for aid in estados:
                estados[aid] = {"estado":"Presente", "justificado":False, "nota":""}
            refrescar()
        def justificar():
            aid = seleccionado()
            if aid is None: return
            nota = simpledialog.askstring("Justificante", "Motivo o referencia del justificante:")
            if nota is None: return
            estados[aid]["estado"] = "Presente"
            estados[aid]["justificado"] = True
            estados[aid]["nota"] = nota.strip()
            refrescar()
            tree.selection_set(str(aid))
        def editar_nombre():
            aid = seleccionado()
            if aid is None: return
            if self.usuario["rol"] != "director":
                messagebox.showinfo("Edición", "Los nombres de alumnos se editan desde el perfil del director.")
                return
            return
        def guardar():
            fecha = fecha_var.get().strip()
            if not fecha_valida(fecha):
                messagebox.showwarning("Fecha inválida", "Escribe una fecha válida con año, mes y día (ejemplo: 2026-10-28).")
                return
            if not alumnos:
                messagebox.showwarning("Lista vacía", "Carga la lista antes de guardar.")
                return
            try:
                filas = []
                for a in alumnos:
                    st = estados[a["id"]]
                    filas.append((a["id"], grupo["id"], self.usuario["id"], fecha,
                                  st["estado"], int(st["justificado"]), st["nota"] or None))
                con = __import__("db").conectar()
                try:
                    cur = con.cursor()
                    cur.executemany(
                        "INSERT INTO asistencias(alumno_id,grupo_id,docente_id,fecha,estado,justificado,nota_justificante) "
                        "VALUES(%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "
                        "grupo_id=VALUES(grupo_id), docente_id=VALUES(docente_id), estado=VALUES(estado), "
                        "justificado=VALUES(justificado), nota_justificante=VALUES(nota_justificante)",
                        filas
                    )
                    con.commit()
                finally:
                    con.close()
                messagebox.showinfo("Guardado", f"Se guardó la asistencia de {len(filas)} alumnos del {grupo['nombre']}.")
            except Exception as exc:
                messagebox.showerror("Error al guardar", str(exc))
        cargar()
    def vista_justificantes(self, parent, grupo):
        tk.Label(parent, text="Registro de justificantes", bg=BG, fg=NAVY,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w", pady=(4,3))
        tk.Label(parent, text="Selecciona al alumno, escribe el motivo y guarda. La falta se corrige a presente justificado.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(0,12))
        bar=tk.Frame(parent,bg=BG); bar.pack(fill="x",pady=5)
        tk.Label(bar,text="Fecha",bg=BG,fg=NAVY,font=("Segoe UI",10,"bold")).pack(side="left")
        fecha=tk.StringVar(value=fecha_hoy())
        tk.Entry(bar,textvariable=fecha,width=14,font=("Segoe UI",11),bg="#254A64",fg="#F6F7F7",relief="solid",bd=1).pack(side="left",padx=8,ipady=4)
        tree=ttk.Treeview(parent,columns=("numero","alumno","estado","justificado","nota"),show="headings",height=13)
        for c,t,w in [("numero","N.º",55),("alumno","Alumno",280),("estado","Estado actual",130),("justificado","Justificado",110),("nota","Motivo",260)]:
            tree.heading(c,text=t); tree.column(c,width=w,anchor="w" if c in ("alumno","nota") else "center")
        tree.pack(fill="both",expand=True,pady=8)
        def cargar():
            f=fecha.get().strip()
            if not fecha_valida(f):
                messagebox.showwarning("Fecha inválida","Escribe una fecha válida con año, mes y día (ejemplo: 2026-10-28).")
                return
            try:
                tree.delete(*tree.get_children())
                rows=consultar("SELECT a.id,a.numero_lista,a.nombre,s.estado,s.justificado,s.nota_justificante "
                               "FROM alumnos a LEFT JOIN asistencias s ON s.alumno_id=a.id AND s.fecha=%s "
                               "WHERE a.grupo_id=%s AND a.activo=1 ORDER BY a.numero_lista",(f,grupo["id"]))
                for r in rows:
                    tree.insert("","end",iid=str(r["id"]),values=(r["numero_lista"],r["nombre"],r["estado"] or "Sin registro",
                        "Sí" if r["justificado"] else "No",r["nota_justificante"] or ""))
            except Exception as exc: messagebox.showerror("Error",str(exc))
        def guardar_justificante():
            sel=tree.selection()
            if not sel:
                messagebox.showinfo("Selecciona un alumno","Selecciona al alumno al que corresponde el justificante."); return
            f=fecha.get().strip()
            if not fecha_valida(f):
                messagebox.showwarning("Fecha inválida","Escribe una fecha válida con año, mes y día (ejemplo: 2026-10-28).")
                return
            nota=simpledialog.askstring("Justificante","Motivo o referencia del justificante:")
            if nota is None: return
            try:
                aid=int(sel[0])
                ejecutar("INSERT INTO asistencias(alumno_id,grupo_id,docente_id,fecha,estado,justificado,nota_justificante) "
                         "VALUES(%s,%s,%s,%s,'Presente',1,%s) ON DUPLICATE KEY UPDATE estado='Presente',justificado=1,nota_justificante=VALUES(nota_justificante),docente_id=VALUES(docente_id)",
                         (aid,grupo["id"],self.usuario["id"],f,nota.strip()))
                cargar()
                tree.selection_set(str(aid))
                messagebox.showinfo("Justificante guardado","Se guardó el justificante y el alumno aparece como Presente justificado.")
            except Exception as exc: messagebox.showerror("Error al guardar",str(exc))
        self.boton(bar,"Cargar",cargar).pack(side="left",padx=4)
        self.boton(parent,"Guardar justificante",guardar_justificante,True).pack(anchor="e",pady=6)
        cargar()
    def vista_conducta(self, parent, grupo):
        form = tk.Frame(parent, bg=WHITE, padx=16, pady=14, highlightbackground=BORDER, highlightthickness=1)
        form.pack(fill="x", pady=8)
        tk.Label(form, text="Registrar incidencia de conducta", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,10))
        alumnos = consultar("SELECT id,nombre FROM alumnos WHERE grupo_id=%s AND activo=1 ORDER BY numero_lista",
                            (grupo["id"],))
        alumno_map = {f"{a['nombre']} (ID {a['id']})": a["id"] for a in alumnos}
        variables = {}
        campos = [
            ("Alumno", "alumno"), ("Título", "titulo"), ("Tipo de incidencia", "tipo"),
            ("Fecha", "fecha"), ("Descripción", "descripcion"), ("Medida que se amerita", "medida")
        ]
        for i,(label,key) in enumerate(campos):
            tk.Label(form, text=label, bg=WHITE, fg=NAVY).grid(row=i+1,column=0,sticky="w",pady=5,padx=(0,12))
            if key == "alumno":
                v = tk.StringVar()
                widget = ttk.Combobox(form, textvariable=v, values=list(alumno_map), state="readonly", width=48)
                if alumno_map: widget.current(0)
            elif key == "descripcion" or key == "medida":
                widget = tk.Text(form, width=50, height=3, font=("Segoe UI",10), relief="solid", bd=1)
                v = widget
            else:
                v = tk.StringVar(value=fecha_hoy() if key=="fecha" else "")
                widget = tk.Entry(form, textvariable=v, width=52, font=("Segoe UI",10), relief="solid", bd=1)
            widget.grid(row=i+1,column=1,sticky="ew",pady=5)
            variables[key] = v
        enviar = tk.IntVar(value=0)
        tk.Checkbutton(form, text="Marcar para seguimiento del tutor", variable=enviar,
                       bg=WHITE, fg=NAVY, activebackground=WHITE).grid(row=7,column=1,sticky="w",pady=6)
        def guardar_incidencia():
            try:
                alumno_label = variables["alumno"].get()
                if not alumno_label: raise ValueError("Selecciona un alumno.")
                alumno_id = alumno_map[alumno_label]
                titulo = variables["titulo"].get().strip()
                tipo = variables["tipo"].get().strip()
                fecha = variables["fecha"].get().strip()
                desc = variables["descripcion"].get("1.0","end").strip()
                medida = variables["medida"].get("1.0","end").strip()
                if not titulo or not tipo or not desc: raise ValueError("Completa título, tipo y descripción.")
                if not fecha_valida(fecha): raise ValueError("La fecha debe tener formato AAAA-MM-DD.")
                ejecutar("INSERT INTO incidencias(alumno_id,grupo_id,docente_id,titulo,descripcion,fecha,tipo,medida,enviar_tutor) "
                         "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (alumno_id,grupo["id"],self.usuario["id"],titulo,desc,fecha,tipo,medida,int(enviar.get())))
                messagebox.showinfo("Incidencia guardada","La incidencia se guardó para revisión de dirección.")
                for key in ("titulo","tipo"):
                    variables[key].set("")
                variables["descripcion"].delete("1.0","end")
                variables["medida"].delete("1.0","end")
            except Exception as exc:
                messagebox.showerror("No se pudo guardar", str(exc))
        self.boton(form, "Guardar incidencia", guardar_incidencia, True).grid(row=8,column=1,sticky="e",pady=(8,0))
    def panel_director(self, parent):
        shell = tk.Frame(parent, bg=BG)
        shell.pack(fill="both", expand=True)
        side = tk.Frame(shell, bg=NAVY, width=215)
        side.pack(side="left", fill="y", padx=(0,14))
        side.pack_propagate(False)
        tk.Label(side, text="CONTROL ESCOLAR", bg=NAVY, fg="#B8E6F6",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=18, pady=(22,6))
        tk.Label(side, text="Dirección", bg=NAVY, fg=WHITE,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(0,22))
        content = tk.Frame(shell, bg=BG)
        content.pack(side="left", fill="both", expand=True)
        vistas = {
            "Resumen y asistencia": self.vista_resumen,
            "Alumnos": self.vista_alumnos,
            "Docentes y grupos": self.vista_docentes,
            "Conducta": self.vista_incidencias,
            "Cartas compromiso": self.vista_cartas,
        }
        def mostrar(nombre):
            for w in content.winfo_children(): w.destroy()
            tk.Label(content, text=nombre, bg=BG, fg=NAVY,
                     font=("Segoe UI", 19, "bold")).pack(anchor="w", pady=(0,7))
            vistas[nombre](content)
        for nombre in vistas:
            self.boton(side, nombre, lambda n=nombre: mostrar(n), nombre == "Resumen y asistencia").pack(fill="x", padx=10, pady=5)
        mostrar("Resumen y asistencia")
    def vista_resumen(self, parent):
        bar = tk.Frame(parent, bg=BG)
        bar.pack(fill="x", pady=8)
        tk.Label(bar, text="Fecha", bg=BG, fg=NAVY).pack(side="left")
        fecha = tk.StringVar(value=fecha_hoy())
        tk.Entry(bar, textvariable=fecha, width=13,bg="#254A64",fg="#F6F7F7",).pack(side="left", padx=8)
        self.boton(bar, "Actualizar", lambda: cargar(), True).pack(side="left")
        cards = tk.Frame(parent, bg=BG)
        cards.pack(fill="x", pady=6)
        labels = {}
        for key,title in [("total","Alumnos activos"),("presentes","Presentes"),("faltas","Faltas"),("retardos","Retardos"),("justificados","Justificadas")]:
            tint = {"total":"#EAF3FC", "presentes":"#E8F7F0", "faltas":"#FFF0F0", "retardos":"#FFF7E6", "justificados":"#EEF0FF"}[key]
            accent = {"total":"#4A83C4", "presentes":"#29966A", "faltas":"#D45E68", "retardos":"#D29B35", "justificados":"#7379C9"}[key]
            card = tk.Frame(cards, bg=tint, highlightbackground=BORDER, highlightthickness=1, padx=16, pady=15)
            card.pack(side="left", fill="both", expand=True, padx=5, pady=3)
            tk.Frame(card, bg=accent, height=4).pack(fill="x", pady=(0,11))
            tk.Label(card, text=title.upper(), bg=tint, fg=MUTED, font=("Segoe UI",9,"bold")).pack(anchor="w")
            labels[key] = tk.Label(card, text="—", bg=tint, fg=accent,
                                   font=("Segoe UI",26,"bold"))
            labels[key].pack(anchor="w", pady=(5,0))
        mid = tk.Frame(parent, bg=BG)
        mid.pack(fill="both", expand=True, pady=8)
        left = tk.Frame(mid, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        left.pack(side="left", fill="both", expand=True, padx=(0,5))
        right = tk.Frame(mid, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        right.pack(side="left", fill="both", expand=True, padx=(5,0))
        tk.Label(left, text="Faltas y retardos por alumno", bg=WHITE, fg=NAVY,
                 font=("Segoe UI",12,"bold")).pack(anchor="w", padx=12, pady=10)
        tree = ttk.Treeview(left, columns=("alumno","grupo","estado","justificado"), show="headings", height=11)
        for c,t,w in [("alumno","Alumno",220),("grupo","Grupo",80),("estado","Estado",90),("justificado","Justificante",95)]:
            tree.heading(c,text=t); tree.column(c,width=w,anchor="w" if c=="alumno" else "center")
        tree.pack(fill="both",expand=True,padx=10,pady=(0,10))
        tk.Label(right, text="Resumen por grupo", bg=WHITE, fg=NAVY,
                 font=("Segoe UI",12,"bold")).pack(anchor="w", padx=12, pady=10)
        chart = tk.Canvas(right, bg=WHITE, highlightthickness=0, height=260)
        chart.pack(fill="both",expand=True,padx=8,pady=4)
        group_tree = ttk.Treeview(right, columns=("grupo","presentes","faltas","retardos"), show="headings", height=6)
        for c,t,w in [("grupo","Grupo",100),("presentes","Presentes",90),("faltas","Faltas",70),("retardos","Retardos",80)]:
            group_tree.heading(c,text=t); group_tree.column(c,width=w,anchor="center")
        group_tree.pack(fill="x",padx=10,pady=(0,10))

        def cargar():
            f = fecha.get().strip()
            if not fecha_valida(f):
                messagebox.showwarning("Fecha inválida","Escribe una fecha válida con año, mes y día (ejemplo: 2026-10-28)."); return
            try:
                total = consultar("SELECT COUNT(*) n FROM alumnos WHERE activo=1")[0]["n"]
                rows = consultar("SELECT estado, COUNT(*) n, SUM(justificado=1) justificados "
                                 "FROM asistencias WHERE fecha=%s GROUP BY estado",(f,))
                counts = {"Presente":0,"Falta":0,"Retardo":0}
                just = 0
                for r in rows:
                    counts[r["estado"]] = r["n"]
                    just += r["justificados"] or 0
                labels["total"].config(text=total)
                labels["presentes"].config(text=counts["Presente"])
                labels["faltas"].config(text=counts["Falta"])
                labels["retardos"].config(text=counts["Retardo"])
                labels["justificados"].config(text=just)
                tree.delete(*tree.get_children())
                listado = consultar("SELECT a.nombre,g.nombre grupo,s.estado,s.justificado "
                                    "FROM asistencias s JOIN alumnos a ON a.id=s.alumno_id "
                                    "JOIN grupos g ON g.id=s.grupo_id WHERE s.fecha=%s "
                                    "AND (s.estado IN ('Falta','Retardo')) ORDER BY g.nombre,a.nombre",(f,))
                for r in listado:
                    tree.insert("", "end", values=(r["nombre"],r["grupo"],r["estado"],
                                                  "Sí" if r["justificado"] else "No"))
                group_tree.delete(*group_tree.get_children())
                por_grupo = consultar(
                    "SELECT g.nombre grupo,"
                    "SUM(s.estado='Presente') presentes,SUM(s.estado='Falta') faltas,"
                    "SUM(s.estado='Retardo') retardos "
                    "FROM grupos g LEFT JOIN asistencias s ON s.grupo_id=g.id AND s.fecha=%s "
                    "WHERE g.activo=1 GROUP BY g.id,g.nombre ORDER BY g.id",(f,))
                chart.delete("all")
                maxval = max([max((r["presentes"] or 0),(r["faltas"] or 0),(r["retardos"] or 0)) for r in por_grupo] or [1])
                for r in por_grupo:
                    group_tree.insert("", "end", values=(r["grupo"],r["presentes"] or 0,r["faltas"] or 0,r["retardos"] or 0))
                width = max(chart.winfo_width(), 360)
                chart.create_text(12,10,text="Presentes   Faltas   Retardos",anchor="nw",fill=MUTED,font=("Segoe UI",9))
                for i,r in enumerate(por_grupo):
                    y=40+i*31
                    chart.create_text(12,y+8,text=r["grupo"],anchor="w",fill=NAVY,font=("Segoe UI",9))
                    x=90
                    for val,col in [(r["presentes"] or 0,"#4F9A75"),(r["faltas"] or 0,"#CF6666"),(r["retardos"] or 0,"#D3A44E")]:
                        w=int((val/30)*max(80,width-160))
                        chart.create_rectangle(x,y,x+w,y+16,fill=col,outline="")
                        x += w+5
            except Exception as exc:
                messagebox.showerror("Error al cargar KPI",str(exc))
        cargar()
    def vista_alumnos(self, parent):
        top = tk.Frame(parent,bg=BG); top.pack(fill="x",pady=8)
        grupos = self.grupos()
        grupo_var = tk.StringVar()
        grupo_map = {g["nombre"]:g["id"] for g in grupos}
        combo = ttk.Combobox(top,textvariable=grupo_var,values=list(grupo_map),state="readonly",width=18)
        combo.pack(side="left",padx=(0,8))
        if grupos: combo.current(0)
        tree = ttk.Treeview(parent,columns=("num","nombre","activo"),show="headings",height=16)
        for c,t,w in [("num","N.º lista",80),("nombre","Nombre del alumno",450),("activo","Activo",90)]:
            tree.heading(c,text=t); tree.column(c,width=w)
        tree.pack(fill="both",expand=True,pady=8)
        def cargar():
            tree.delete(*tree.get_children())
            gid=grupo_map.get(grupo_var.get())
            if not gid:return
            for a in consultar("SELECT id,numero_lista,nombre,activo FROM alumnos WHERE grupo_id=%s ORDER BY numero_lista",(gid,)):
                tree.insert("", "end", iid=str(a["id"]),values=(a["numero_lista"],a["nombre"],"Sí" if a["activo"] else "No"))
        def editar():
            sel=tree.selection()
            if not sel: messagebox.showinfo("Selecciona","Selecciona un alumno.");return
            aid=int(sel[0])
            actual=tree.item(sel[0],"values")[1]
            nuevo=simpledialog.askstring("Editar alumno","Nombre completo:",initialvalue=actual)
            if nuevo and nuevo.strip():
                ejecutar("UPDATE alumnos SET nombre=%s WHERE id=%s",(nuevo.strip(),aid));cargar()
        def cambiar_activo():
            sel=tree.selection()
            if not sel: messagebox.showinfo("Selecciona","Selecciona un alumno.");return
            aid=int(sel[0]); actual=tree.item(sel[0],"values")[2]=="Sí"
            ejecutar("UPDATE alumnos SET activo=%s WHERE id=%s",(0 if actual else 1,aid));cargar()
        self.boton(top,"Actualizar",cargar).pack(side="left",padx=3)
        self.boton(top,"Editar nombre",editar,True).pack(side="left",padx=3)
        self.boton(top,"Activar/desactivar",cambiar_activo).pack(side="left",padx=3)
        combo.bind("<<ComboboxSelected>>",lambda e:cargar())
        cargar()
    def vista_docentes(self, parent):
        top=tk.Frame(parent,bg=BG);top.pack(fill="x",pady=8)
        tree=ttk.Treeview(parent,columns=("usuario","nombre","grupo","activo"),show="headings",height=16)
        for c,t,w in [("usuario","Usuario",130),("nombre","Nombre del docente",300),("grupo","Grupo asignado",150),("activo","Activo",80)]:
            tree.heading(c,text=t);tree.column(c,width=w)
        tree.pack(fill="both",expand=True,pady=8)
        def cargar():
            tree.delete(*tree.get_children())
            for r in consultar("SELECT u.id,u.usuario,u.nombre,u.activo,g.nombre grupo FROM usuarios u "
                               "LEFT JOIN grupos g ON g.docente_id=u.id WHERE u.rol='docente' ORDER BY u.usuario"):
                tree.insert("", "end",iid=str(r["id"]),values=(r["usuario"],r["nombre"],r["grupo"] or "Sin asignar","Sí" if r["activo"] else "No"))
        def editar():
            sel=tree.selection()
            if not sel: messagebox.showinfo("Selecciona","Selecciona un docente.");return
            uid=int(sel[0]); vals=tree.item(sel[0],"values")
            nombre=simpledialog.askstring("Editar docente","Nombre para mostrar:",initialvalue=vals[1])
            if not nombre or not nombre.strip():return
            grupos=self.grupos()
            opciones=[g["nombre"] for g in grupos]
            grupo=simpledialog.askstring("Asignar grupo","Escribe exactamente uno de estos grupos:\n"+", ".join(opciones),initialvalue=vals[2] if vals[2]!="Sin asignar" else "")
            if grupo and grupo not in opciones:
                messagebox.showwarning("Grupo no válido","El grupo debe coincidir con uno de la lista.");return
            ejecutar("UPDATE usuarios SET nombre=%s WHERE id=%s",(nombre.strip(),uid))
            if grupo:
                gid=next(g["id"] for g in grupos if g["nombre"]==grupo)
                ejecutar("UPDATE grupos SET docente_id=NULL WHERE docente_id=%s AND id<>%s",(uid,gid))
                ejecutar("UPDATE grupos SET docente_id=NULL WHERE id=%s AND docente_id<>%s",(gid,uid))
                ejecutar("UPDATE grupos SET docente_id=%s WHERE id=%s",(uid,gid))
            cargar()
        def toggle():
            sel=tree.selection()
            if not sel:return
            uid=int(sel[0]); activo=tree.item(sel[0],"values")[3]=="Sí"
            ejecutar("UPDATE usuarios SET activo=%s WHERE id=%s",(0 if activo else 1,uid));cargar()
        self.boton(top,"Actualizar",cargar).pack(side="left",padx=3)
        self.boton(top,"Editar nombre / grupo",editar,True).pack(side="left",padx=3)
        self.boton(top,"Activar/desactivar",toggle).pack(side="left",padx=3)
        cargar()
    def vista_incidencias(self, parent):
        """Lista de conducta que aprovecha todo el espacio disponible."""
        top = tk.Frame(parent, bg=BG)
        top.pack(fill="x", pady=(4, 10))
        info = tk.Frame(top, bg=BG)
        info.pack(side="left", fill="x", expand=True)
        tk.Label(info, text="Seguimiento de conducta", bg=BG, fg=NAVY,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w")
        tk.Label(info, text="Consulta las incidencias registradas por grupo, alumno y fecha.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 0))
        self.boton(top, "Actualizar incidencias", lambda: cargar(), True).pack(side="right", padx=(8, 0))

        card = tk.Frame(parent, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, pady=(0, 2))
        table_area = tk.Frame(card, bg=WHITE)
        table_area.pack(fill="both", expand=True, padx=8, pady=8)
        columns = ("fecha", "alumno", "grupo", "titulo", "tipo", "descripcion", "medida", "docente")
        tree = ttk.Treeview(table_area, columns=columns, show="headings", selectmode="browse")
        for c, t, w in [
            ("fecha", "Fecha", 100), ("alumno", "Alumno", 190), ("grupo", "Grupo", 85),
            ("titulo", "Título", 155), ("tipo", "Tipo", 110),
            ("descripcion", "Descripción", 240), ("medida", "Medida / seguimiento", 200),
            ("docente", "Docente", 150)
        ]:
            tree.heading(c, text=t)
            tree.column(c, width=w, minwidth=70, anchor="w" if c not in ("fecha", "grupo") else "center", stretch=True)
        yscroll = ttk.Scrollbar(table_area, orient="vertical", command=tree.yview)
        xscroll = ttk.Scrollbar(card, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        table_area.rowconfigure(0, weight=1)
        table_area.columnconfigure(0, weight=1)
        tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.pack(fill="x", padx=8, pady=(0, 8))
        tree.tag_configure("par", background="#F7FAFC")
        tree.tag_configure("impar", background=WHITE)

        def cargar():
            try:
                tree.delete(*tree.get_children())
                rows = consultar(
                    "SELECT i.fecha,a.nombre alumno,g.nombre grupo,i.titulo,i.tipo,i.descripcion,i.medida,u.nombre docente "
                    "FROM incidencias i JOIN alumnos a ON a.id=i.alumno_id JOIN grupos g ON g.id=i.grupo_id "
                    "JOIN usuarios u ON u.id=i.docente_id ORDER BY i.fecha DESC,i.id DESC"
                )
                for i, r in enumerate(rows):
                    tree.insert("", "end", values=(r["fecha"], r["alumno"], r["grupo"], r["titulo"],
                               r["tipo"], r["descripcion"], r["medida"] or "—", r["docente"]),
                               tags=("par" if i % 2 == 0 else "impar",))
            except Exception as exc:
                messagebox.showerror("Error al cargar incidencias", str(exc))
        cargar()

    def vista_cartas(self, parent):
        form=tk.Frame(parent,bg=WHITE,padx=14,pady=12,highlightbackground=BORDER,highlightthickness=1)
        form.pack(fill="x",pady=8)
        tk.Label(form,text="Registrar carta compromiso",bg=WHITE,fg=NAVY,font=("Segoe UI",13,"bold")).grid(row=0,column=0,columnspan=4,sticky="w",pady=(0,8))
        grupos=self.grupos()
        grupo_map={g["nombre"]:g["id"] for g in grupos}
        gvar=tk.StringVar(value=next(iter(grupo_map),""))
        tk.Label(form,text="Grupo",bg=WHITE,fg=NAVY).grid(row=1,column=0,sticky="w",padx=5,pady=4)
        gcombo=ttk.Combobox(form,textvariable=gvar,values=list(grupo_map),state="readonly",width=18)
        gcombo.grid(row=1,column=1,sticky="w",padx=5,pady=4)
        tk.Label(form,text="Alumno",bg=WHITE,fg=NAVY).grid(row=1,column=2,sticky="w",padx=5,pady=4)
        avar=tk.StringVar()
        acombo=ttk.Combobox(form,textvariable=avar,state="readonly",width=32)
        acombo.grid(row=1,column=3,sticky="w",padx=5,pady=4)
        alumnos_map={}
        def cargar_alumnos(event=None):
            alumnos=consultar("SELECT id,nombre FROM alumnos WHERE grupo_id=%s AND activo=1 ORDER BY numero_lista",(grupo_map[gvar.get()],))
            alumnos_map.clear();alumnos_map.update({a["nombre"]:a["id"] for a in alumnos})
            acombo["values"]=list(alumnos_map)
            if alumnos: acombo.current(0)
        gcombo.bind("<<ComboboxSelected>>",cargar_alumnos);cargar_alumnos()
        vars={}
        for row,(lab,key) in enumerate([("Fecha","fecha"),("Título","titulo"),("Motivo / incidencia","motivo"),("Compromisos acordados","compromisos"),("Seguimiento (opcional)","seguimiento")],start=2):
            tk.Label(form,text=lab,bg=WHITE,fg=NAVY).grid(row=row,column=0,sticky="w",padx=5,pady=4)
            if key in ("motivo","compromisos"):
                w=tk.Text(form,width=65,height=2,font=("Segoe UI",10),relief="solid",bd=1)
                w.grid(row=row,column=1,columnspan=3,sticky="ew",padx=5,pady=4);vars[key]=w
            else:
                v=tk.StringVar(value=fecha_hoy() if key=="fecha" else "")
                w=tk.Entry(form,textvariable=v,width=67,font=("Segoe UI",10),relief="solid",bd=1)
                w.grid(row=row,column=1,columnspan=3,sticky="ew",padx=5,pady=4);vars[key]=v
        def guardar():
            try:
                gid=grupo_map.get(gvar.get());aid=alumnos_map.get(avar.get())
                f=vars["fecha"].get().strip(); titulo=vars["titulo"].get().strip()
                motivo=vars["motivo"].get("1.0","end").strip()
                compromisos=vars["compromisos"].get("1.0","end").strip()
                seguimiento=vars["seguimiento"].get().strip() or None
                if not gid or not aid: raise ValueError("Selecciona grupo y alumno.")
                if not fecha_valida(f) or (seguimiento and not fecha_valida(seguimiento)): raise ValueError("Revisa las fechas.")
                if not titulo or not motivo or not compromisos: raise ValueError("Completa título, motivo y compromisos.")
                ejecutar("INSERT INTO cartas_compromiso(alumno_id,grupo_id,director_id,fecha,titulo,motivo,compromisos,fecha_seguimiento) "
                         "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                         (aid,gid,self.usuario["id"],f,titulo,motivo,compromisos,seguimiento))
                messagebox.showinfo("Carta registrada","La carta compromiso se guardó correctamente.")
                vars["titulo"].set("");vars["motivo"].delete("1.0","end");vars["compromisos"].delete("1.0","end")
                cargar_cartas()
            except Exception as exc: messagebox.showerror("Error",str(exc))
        self.boton(form,"Guardar carta",guardar,True).grid(row=7,column=1,sticky="e",pady=8)
        lista=tk.Frame(parent,bg=BG);lista.pack(fill="both",expand=True)
        tree=ttk.Treeview(lista,columns=("fecha","alumno","grupo","titulo","estado","seguimiento"),show="headings",height=8)
        for c,t,w in [("fecha","Fecha",90),("alumno","Alumno",180),("grupo","Grupo",90),("titulo","Título",210),("estado","Estado",130),("seguimiento","Seguimiento",120)]:
            tree.heading(c,text=t);tree.column(c,width=w)
        tree.pack(fill="both",expand=True,pady=6)
        def cargar_cartas():
            tree.delete(*tree.get_children())
            for r in consultar("SELECT c.id,c.fecha,a.nombre alumno,g.nombre grupo,c.titulo,c.estado,c.fecha_seguimiento "
                               "FROM cartas_compromiso c JOIN alumnos a ON a.id=c.alumno_id "
                               "JOIN grupos g ON g.id=c.grupo_id ORDER BY c.fecha DESC,c.id DESC"):
                tree.insert("", "end",iid=str(r["id"]),values=(r["fecha"],r["alumno"],r["grupo"],r["titulo"],r["estado"],r["fecha_seguimiento"] or "—"))
        def cambiar_estado():
            sel=tree.selection()
            if not sel:messagebox.showinfo("Selecciona","Selecciona una carta.");return
            estado=simpledialog.askstring("Estado de carta","Escribe: Pendiente, En seguimiento, Cumplida o Cerrada",
                                             initialvalue=tree.item(sel[0],"values")[4])
            permitidos=("Pendiente","En seguimiento","Cumplida","Cerrada")
            if estado not in permitidos:messagebox.showwarning("Estado inválido","Elige un estado válido.");return
            ejecutar("UPDATE cartas_compromiso SET estado=%s WHERE id=%s",(estado,int(sel[0])));cargar_cartas()
        self.boton(lista,"Actualizar cartas",cargar_cartas).pack(side="left",padx=4)
        self.boton(lista,"Cambiar estado",cambiar_estado,True).pack(side="left",padx=4)
        cargar_cartas()
