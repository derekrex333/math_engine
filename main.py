"""
Math Engine — Punto de entrada principal.
Menú navegable por categorías, subcategorías y métodos.
"""

import importlib


# Estructura completa del proyecto:
# { "Nombre categoría": { "Nombre subcategoría": [ ("Nombre método", "ruta.modulo") ] } }

MENU = {
    "Métodos Numéricos": 
    {
        "Raíces de ecuaciones": 
        [
            ("Bisección",      "metodos_numericos.raices_ecuaciones.biseccion"),
            ("Falsa posición", "metodos_numericos.raices_ecuaciones.falsa_posicion"),
            ("Secante",        "metodos_numericos.raices_ecuaciones.secante"),
            ("Newton-Raphson", "metodos_numericos.raices_ecuaciones.newton_raphson"),
            ("Punto fijo",     "metodos_numericos.raices_ecuaciones.punto_fijo"),
            ("Müller",         "metodos_numericos.raices_ecuaciones.muller"),
            ("Aberth-Ehrlich", "metodos_numericos.raices_ecuaciones.aberth_ehrlich"),
        ],
        "Interpolación": 
        [
            ("Lagrange",                     "metodos_numericos.interpolacion.lagrange"),
            ("Newton diferencias divididas", "metodos_numericos.interpolacion.newton_diferencias_divididas"),
            ("Spline lineal",                "metodos_numericos.interpolacion.spline_lineal"),
            ("Spline cúbico",                "metodos_numericos.interpolacion.spline_cubico"),
            ("Hermite",                      "metodos_numericos.interpolacion.hermite"),
            ("Racional",                     "metodos_numericos.interpolacion.racional"),
        ],
        "Integración numérica": 
        [
            ("Trapecio",             "metodos_numericos.integracion_numerica.trapecio"),
            ("Simpson 1/3",          "metodos_numericos.integracion_numerica.simpson_1_3"),
            ("Simpson 3/8",          "metodos_numericos.integracion_numerica.simpson_3_8"),
            ("Cuadratura gaussiana", "metodos_numericos.integracion_numerica.cuadratura_gaussiana"),
            ("Romberg",              "metodos_numericos.integracion_numerica.romberg"),
            ("Monte Carlo",          "metodos_numericos.integracion_numerica.montecarlo"),
            ("Integral doble",       "metodos_numericos.integracion_numerica.integral_doble"),
            ("Integral triple",      "metodos_numericos.integracion_numerica.integral_triple"),
        ],
        "Ecuaciones diferenciales": 
        [
            ("Euler",                      "metodos_numericos.ecuaciones_diferenciales.euler"),
            ("Euler mejorado (Heun)",      "metodos_numericos.ecuaciones_diferenciales.euler_mejorado"),
            ("Runge-Kutta 2",              "metodos_numericos.ecuaciones_diferenciales.runge_kutta_2"),
            ("Runge-Kutta 4",              "metodos_numericos.ecuaciones_diferenciales.runge_kutta_4"),
            ("Runge-Kutta-Fehlberg",       "metodos_numericos.ecuaciones_diferenciales.runge_kutta_fehlberg"),
            ("Dormand-Prince (RK45)",      "metodos_numericos.ecuaciones_diferenciales.dormand_prince"),
            ("Sistemas de EDOs",           "metodos_numericos.ecuaciones_diferenciales.sistemas_edos"),
            ("EDOs de orden superior",     "metodos_numericos.ecuaciones_diferenciales.edos_orden_superior"),
            ("Condiciones de borde",       "metodos_numericos.ecuaciones_diferenciales.condiciones_borde"),
            ("PDE parabólicas (calor 1D)", "metodos_numericos.ecuaciones_diferenciales.pde_parabolicas"),
            ("PDE elípticas (Laplace)",    "metodos_numericos.ecuaciones_diferenciales.pde_elipticas"),
        ],
    },

    "Álgebra Lineal": 
    {
        "Matrices": 
        [
            ("Suma",                   "algebra_lineal.matrices.suma"),
            ("Multiplicación",         "algebra_lineal.matrices.multiplicacion"),
            ("Inversa",                "algebra_lineal.matrices.inversa"),
            ("Determinante",           "algebra_lineal.matrices.determinante"),
            ("Potencia",               "algebra_lineal.matrices.potencia"),
            ("Transpuesta",            "algebra_lineal.matrices.transpuesta"),
            ("Rango",                  "algebra_lineal.matrices.rango"),
            ("Traza",                  "algebra_lineal.matrices.traza"),
            ("Normas",                 "algebra_lineal.matrices.normas"),
            ("Factorización LU",       "algebra_lineal.matrices.factorizacion_lu"),
            ("Factorización QR",       "algebra_lineal.matrices.factorizacion_qr"),
            ("Factorización Cholesky", "algebra_lineal.matrices.factorizacion_cholesky"),
            ("SVD",                    "algebra_lineal.matrices.svd"),
            ("Autovalores (potencia)", "algebra_lineal.matrices.autovalores_potencia"),
            ("Autovalores (QR)",       "algebra_lineal.matrices.autovalores_qr"),
        ],
        "Sistemas lineales": 
        [
            ("Gauss",                  "algebra_lineal.sistemas_lineales.gauss"),
            ("Gauss-Jordan",           "algebra_lineal.sistemas_lineales.gauss_jordan"),
            ("Jacobi",                 "algebra_lineal.sistemas_lineales.jacobi"),
            ("Gauss-Seidel",           "algebra_lineal.sistemas_lineales.gauss_seidel"),
            ("SOR",                    "algebra_lineal.sistemas_lineales.sor"),
            ("Gradiente conjugado",    "algebra_lineal.sistemas_lineales.gradiente_conjugado"),
            ("Sistemas tridiagonales", "algebra_lineal.sistemas_lineales.sistemas_tridiagonales"),
        ],
    },

    "Cálculo": 
    {
        "Límites": 
        [
            ("Límite numérico",   "calculo.limites.limite_numerico"),
            ("Límite simbólico",  "calculo.limites.limite_simbolico"),
            ("Límites laterales", "calculo.limites.limites_laterales"),
            ("Límites infinitos", "calculo.limites.limites_infinitos"),
        ],
        "Derivadas": 
        [
            ("Simbólicas",          "calculo.derivadas.simbolicas"),
            ("Numéricas",           "calculo.derivadas.numericas"),
            ("Diferencias finitas", "calculo.derivadas.diferencias_finitas"),
            ("Derivadas parciales", "calculo.derivadas.derivadas_parciales"),
            ("Gradiente",           "calculo.derivadas.gradiente"),
            ("Jacobiano",           "calculo.derivadas.jacobiano"),
            ("Hessiano",            "calculo.derivadas.hessiano"),
        ],
        "Integrales": 
        [
            ("Definidas",               "calculo.integrales.definidas"),
            ("Indefinidas",             "calculo.integrales.indefinidas"),
            ("Impropias",               "calculo.integrales.integrales_impropias"),
            ("De línea",                "calculo.integrales.integrales_linea"),
            ("De superficie",           "calculo.integrales.integrales_superficie"),
            ("De volumen",              "calculo.integrales.integrales_volumen"),
            ("Series de Taylor",        "calculo.integrales.series_taylor"),
            ("Series de Fourier",       "calculo.integrales.series_fourier"),
            ("Transformada de Fourier", "calculo.integrales.transformada_fourier"),
            ("Transformada de Laplace", "calculo.integrales.transformada_laplace"),
        ],
    },

    "Probabilidad y Estadística": 
    {
        "Estadística descriptiva": 
        [
            ("Media",               "probabilidad_estadistica.estadistica_descriptiva.media"),
            ("Mediana",             "probabilidad_estadistica.estadistica_descriptiva.mediana"),
            ("Moda",                "probabilidad_estadistica.estadistica_descriptiva.moda"),
            ("Varianza",            "probabilidad_estadistica.estadistica_descriptiva.varianza"),
            ("Desviación estándar", "probabilidad_estadistica.estadistica_descriptiva.desviacion_estandar"),
            ("Rango",               "probabilidad_estadistica.estadistica_descriptiva.rango"),
            ("Cuartiles",           "probabilidad_estadistica.estadistica_descriptiva.cuartiles"),
            ("Percentiles",         "probabilidad_estadistica.estadistica_descriptiva.percentiles"),
            ("Asimetría",           "probabilidad_estadistica.estadistica_descriptiva.asimetria"),
            ("Curtosis",            "probabilidad_estadistica.estadistica_descriptiva.curtosis"),
            ("Correlación",         "probabilidad_estadistica.estadistica_descriptiva.correlacion"),
            ("Covarianza",          "probabilidad_estadistica.estadistica_descriptiva.covarianza"),
            ("Histograma",          "probabilidad_estadistica.estadistica_descriptiva.histograma"),
            ("Boxplot",             "probabilidad_estadistica.estadistica_descriptiva.boxplot"),
        ],
        "Distribuciones": 
        [
            ("Normal",             "probabilidad_estadistica.distribuciones.normal"),
            ("Binomial",           "probabilidad_estadistica.distribuciones.binomial"),
            ("Poisson",            "probabilidad_estadistica.distribuciones.poisson"),
            ("Uniforme",           "probabilidad_estadistica.distribuciones.uniforme"),
            ("Exponencial",        "probabilidad_estadistica.distribuciones.exponencial"),
            ("Gamma",              "probabilidad_estadistica.distribuciones.gamma"),
            ("Beta",               "probabilidad_estadistica.distribuciones.beta"),
            ("Chi cuadrado",       "probabilidad_estadistica.distribuciones.chi_cuadrado"),
            ("t de Student",       "probabilidad_estadistica.distribuciones.t_student"),
            ("F de Fisher",        "probabilidad_estadistica.distribuciones.f_fisher"),
            ("Log-normal",         "probabilidad_estadistica.distribuciones.lognormal"),
            ("Weibull",            "probabilidad_estadistica.distribuciones.weibull"),
            ("Muestreo aleatorio", "probabilidad_estadistica.distribuciones.muestreo_aleatorio"),
        ],
        "Inferencia": 
        [
            ("Intervalos de confianza", "probabilidad_estadistica.inferencia.intervalos_confianza"),
            ("Pruebas de hipótesis",    "probabilidad_estadistica.inferencia.pruebas_hipotesis"),
            ("Prueba Z",                "probabilidad_estadistica.inferencia.prueba_z"),
            ("Prueba T",                "probabilidad_estadistica.inferencia.prueba_t"),
            ("ANOVA",                   "probabilidad_estadistica.inferencia.anova"),
            ("Prueba Chi cuadrado",     "probabilidad_estadistica.inferencia.prueba_chi_cuadrado"),
            ("Regresión lineal",        "probabilidad_estadistica.inferencia.regresion_lineal"),
            ("Regresión múltiple",      "probabilidad_estadistica.inferencia.regresion_multiple"),
            ("Bootstrap",               "probabilidad_estadistica.inferencia.bootstrap"),
            ("Bayes",                   "probabilidad_estadistica.inferencia.bayes"),
            ("MLE",                     "probabilidad_estadistica.inferencia.mle"),
        ],
    },

    "Optimización": 
    {
        "Optimización 1D": 
        [
            ("Búsqueda dorada",          "optimizacion.optimizacion_1d.busqueda_dorada"),
            ("Bisección de mínimos",     "optimizacion.optimizacion_1d.biseccion_minimos"),
            ("Fibonacci",                "optimizacion.optimizacion_1d.fibonacci"),
            ("Interpolación cuadrática", "optimizacion.optimizacion_1d.interpolacion_cuadratica"),
            ("Newton 1D",                "optimizacion.optimizacion_1d.newton_1d"),
        ],
        "Optimización multivariable": 
        [
            ("Gradiente descendente",    "optimizacion.optimizacion_multivariable.gradiente_descendente"),
            ("Newton",                   "optimizacion.optimizacion_multivariable.newton"),
            ("Gradiente conjugado",      "optimizacion.optimizacion_multivariable.gradiente_conjugado"),
            ("BFGS",                     "optimizacion.optimizacion_multivariable.bfgs"),
            ("L-BFGS",                   "optimizacion.optimizacion_multivariable.lbfgs"),
            ("Adam",                     "optimizacion.optimizacion_multivariable.adam"),
            ("Optimización restringida", "optimizacion.optimizacion_multivariable.optimizacion_restricta"),
            ("Programación lineal",      "optimizacion.optimizacion_multivariable.programacion_lineal"),
            ("SQP",                      "optimizacion.optimizacion_multivariable.cuadratica_secuencial"),
            ("Algoritmos genéticos",     "optimizacion.optimizacion_multivariable.algoritmos_geneticos"),
            ("Recocido simulado",        "optimizacion.optimizacion_multivariable.recocido_simulado"),
            ("PSO (partículas)",         "optimizacion.optimizacion_multivariable.optimizacion_particulas"),
        ],
    },

    "Matemáticas Discretas": 
    {
        "Lógica": 
        [
            ("Tablas de verdad",      "matematicas_discretas.logica.tablas_verdad"),
            ("Equivalencias lógicas", "matematicas_discretas.logica.equivalencias_logicas"),
            ("Cuantificadores",       "matematicas_discretas.logica.cuantificadores"),
            ("Demostraciones",        "matematicas_discretas.logica.demostraciones"),
        ],
        "Combinatoria": 
        [
            ("Permutaciones",                 "matematicas_discretas.combinatoria.permutaciones"),
            ("Combinaciones",                 "matematicas_discretas.combinatoria.combinaciones"),
            ("Variaciones",                   "matematicas_discretas.combinatoria.variaciones"),
            ("Coeficientes binomiales",       "matematicas_discretas.combinatoria.coeficientes_binomiales"),
            ("Particiones",                   "matematicas_discretas.combinatoria.particiones"),
            ("Principio inclusión-exclusión", "matematicas_discretas.combinatoria.principio_inclusion_exclusion"),
        ],
        "Teoría de números": 
        [
            ("MCD y MCM",               "matematicas_discretas.teoria_numeros.mcd_mcm"),
            ("Criba de Eratóstenes",    "matematicas_discretas.teoria_numeros.criba_eratostenes"),
            ("Factorización en primos", "matematicas_discretas.teoria_numeros.factorizacion_primos"),
            ("Congruencias",            "matematicas_discretas.teoria_numeros.congruencias"),
            ("Teorema chino del resto", "matematicas_discretas.teoria_numeros.teorema_chino_resto"),
            ("Phi de Euler",            "matematicas_discretas.teoria_numeros.phi_euler"),
            ("Logaritmo discreto",      "matematicas_discretas.teoria_numeros.logaritmo_discreto"),
            ("RSA",                     "matematicas_discretas.teoria_numeros.rsa"),
        ],
    },

    "Teoría de Grafos": 
    {
        "Representaciones": 
        [
            ("Matriz de adyacencia", "teoria_grafos.representaciones.matriz_adyacencia"),
            ("Lista de adyacencia",  "teoria_grafos.representaciones.lista_adyacencia"),
            ("Matriz de incidencia", "teoria_grafos.representaciones.matriz_incidencia"),
        ],
        "Recorridos": 
        [
            ("BFS",              "teoria_grafos.recorridos.bfs"),
            ("DFS",              "teoria_grafos.recorridos.dfs"),
            ("Orden topológico", "teoria_grafos.recorridos.topological_sort"),
        ],
        "Caminos mínimos": 
        [
            ("Dijkstra",       "teoria_grafos.caminos_minimos.dijkstra"),
            ("Bellman-Ford",   "teoria_grafos.caminos_minimos.bellman_ford"),
            ("Floyd-Warshall", "teoria_grafos.caminos_minimos.floyd_warshall"),
            ("A*",             "teoria_grafos.caminos_minimos.a_estrella"),
            ("Johnson",        "teoria_grafos.caminos_minimos.johnson"),
        ],
        "Árboles de expansión": 
        [
            ("Prim",           "teoria_grafos.arboles.prim"),
            ("Kruskal",        "teoria_grafos.arboles.kruskal"),
            ("Borůvka",        "teoria_grafos.arboles.boruvka"),
            ("Árbol con raíz", "teoria_grafos.arboles.arbol_raiz"),
        ],
        "Flujos": 
        [
            ("Ford-Fulkerson", "teoria_grafos.flujos.ford_fulkerson"),
            ("Edmonds-Karp",   "teoria_grafos.flujos.edmonds_karp"),
            ("Dinic",          "teoria_grafos.flujos.dinic"),
        ],
        "Coloración": 
        [
            ("Greedy coloring", "teoria_grafos.coloracion.greedy_coloring"),
            ("Welsh-Powell",    "teoria_grafos.coloracion.welsh_powell"),
        ],
    },

    "Análisis de Datos": 
    {
        "Procesamiento": 
        [
            ("Limpieza",                     "analisis_datos.procesamiento.limpieza"),
            ("Transformación",               "analisis_datos.procesamiento.transformacion"),
            ("Normalización",                "analisis_datos.procesamiento.normalizacion"),
            ("Estandarización",              "analisis_datos.procesamiento.estandarizacion"),
            ("Imputación",                   "analisis_datos.procesamiento.imputacion"),
            ("Detección de outliers",        "analisis_datos.procesamiento.deteccion_outliers"),
            ("Reducción de dimensionalidad", "analisis_datos.procesamiento.reduccion_dimensionalidad"),
            ("Selección de características", "analisis_datos.procesamiento.seleccion_caracteristicas"),
        ],
        "Visualización": 
        [
            ("Gráficas básicas",      "analisis_datos.visualizacion.graficas_basicas"),
            ("Gráficas avanzadas",    "analisis_datos.visualizacion.graficas_avanzadas"),
            ("Mapas de calor",        "analisis_datos.visualizacion.mapas_calor"),
            ("Gráficos 3D",           "analisis_datos.visualizacion.graficos_3d"),
            ("Gráficos interactivos", "analisis_datos.visualizacion.graficos_interactivos"),
            ("Series temporales",     "analisis_datos.visualizacion.series_temporales"),
        ],
    },

    "Machine Learning": 
    {
        "Preprocesamiento": 
        [
            ("Train-test split",   "machine_learning.preprocesamiento.train_test_split"),
            ("Validación cruzada", "machine_learning.preprocesamiento.cross_validation"),
            ("Feature scaling",    "machine_learning.preprocesamiento.feature_scaling"),
        ],
        "Supervisado": 
        [
            ("Regresión lineal",       "machine_learning.supervisado.regresion_lineal"),
            ("Regresión polinomial",   "machine_learning.supervisado.regresion_polinomial"),
            ("Regresión logística",    "machine_learning.supervisado.regresion_logistica"),
            ("KNN",                    "machine_learning.supervisado.knn"),
            ("SVM",                    "machine_learning.supervisado.svm"),
            ("Árboles de decisión",    "machine_learning.supervisado.arboles_decision"),
            ("Random Forest",          "machine_learning.supervisado.random_forest"),
            ("Gradient Boosting",      "machine_learning.supervisado.gradient_boosting"),
            ("Naive Bayes",            "machine_learning.supervisado.naive_bayes"),
            ("Redes neuronales (MLP)", "machine_learning.supervisado.redes_neuronales"),
        ],
        "No supervisado": 
        [
            ("K-Means",                "machine_learning.no_supervisado.kmeans"),
            ("K-Medoids",              "machine_learning.no_supervisado.kmedoids"),
            ("DBSCAN",                 "machine_learning.no_supervisado.dbscan"),
            ("Clustering jerárquico",  "machine_learning.no_supervisado.hierarchical_clustering"),
            ("Mezcla gaussiana (GMM)", "machine_learning.no_supervisado.gaussian_mixture"),
            ("PCA",                    "machine_learning.no_supervisado.pca"),
            ("t-SNE",                  "machine_learning.no_supervisado.tsne"),
            ("Autoencoders",           "machine_learning.no_supervisado.autoencoders"),
            ("Reglas de asociación",   "machine_learning.no_supervisado.reglas_asociacion"),
        ],
    },

    "Series de Tiempo": 
    {
        "Métodos": 
        [
            ("Descomposición",            "series_tiempo.descomposicion"),
            ("Autocorrelación",           "series_tiempo.autocorrelacion"),
            ("ARIMA",                     "series_tiempo.arima"),
            ("SARIMA",                    "series_tiempo.sarima"),
            ("Suavizamiento exponencial", "series_tiempo.suavizamiento_exponencial"),
            ("Prophet",                   "series_tiempo.prophet"),
            ("LSTM temporal",             "series_tiempo.lstm_temporal"),
        ],
    },

    "Procesamiento de Señales": 
    {
        "Métodos": 
        [
            ("Convolución",       "procesamiento_senales.convolucion"),
            ("Correlación",       "procesamiento_senales.correlacion"),
            ("Filtros (FIR/IIR)", "procesamiento_senales.filtros"),
            ("FFT",               "procesamiento_senales.fft"),
            ("Wavelets",          "procesamiento_senales.wavelets"),
            ("Espectrograma",     "procesamiento_senales.espectrograma"),
        ],
    },

    "Métodos Científicos": 
    {
        "Métodos": 
        [
            ("Simulación Monte Carlo",       "metodos_cientificos.simulacion_montecarlo"),
            ("Dinámica molecular",           "metodos_cientificos.dinamica_molecular"),
            ("Elementos finitos (FEM)",      "metodos_cientificos.elementos_finitos"),
            ("Volúmenes finitos (FVM)",      "metodos_cientificos.volumenes_finitos"),
            ("Diferencias finitas avanzado", "metodos_cientificos.diferencias_finitas_avanzado"),
            ("Métodos de malla",             "metodos_cientificos.metodos_malla"),
        ],
    },

    "Optimización Combinatoria": 
    {
        "Métodos": 
        [
            ("Problema de la mochila",      "optimizacion_combinatoria.problema_mochila"),
            ("Problema del viajero (TSP)",  "optimizacion_combinatoria.problema_viajero"),
            ("Asignación de tareas",        "optimizacion_combinatoria.asignacion_tareas"),
            ("Branch and Bound",            "optimizacion_combinatoria.branch_and_bound"),
            ("Programación dinámica",       "optimizacion_combinatoria.programacion_dinamica"),
            ("Colonia de hormigas",         "optimizacion_combinatoria.colonia_hormigas"),
            ("Enjambre de abejas",          "optimizacion_combinatoria.enjambre_abejas"),
        ],
    },

    "Finanzas Cuantitativas": 
    {
        "Métodos": 
        [
            ("VAN y TIR",                            "finanzas_cuantitativas.van_tir"),
            ("Amortización",                         "finanzas_cuantitativas.amortizacion"),
            ("Opciones financieras (Black-Scholes)", "finanzas_cuantitativas.opciones_financieras"),
            ("VaR (Value at Risk)",                  "finanzas_cuantitativas.var_riesgo"),
            ("Monte Carlo financiero",               "finanzas_cuantitativas.simulacion_montecarlo_fin"),
            ("Modelos de volatilidad (GARCH)",       "finanzas_cuantitativas.modelos_volatilidad"),
        ],
    },

    "Procesamiento de Lenguaje Natural": 
    {
        "Métodos": 
        [
            ("Tokenización",                "procesamiento_lenguaje_natural.tokenizacion"),
            ("Stemming / Lematización",     "procesamiento_lenguaje_natural.stemming_lemmatization"),
            ("TF-IDF",                      "procesamiento_lenguaje_natural.tf_idf"),
            ("Word Embeddings (Word2Vec)",  "procesamiento_lenguaje_natural.word_embeddings"),
            ("Análisis de sentimiento",     "procesamiento_lenguaje_natural.analisis_sentimiento"),
            ("Clasificación de texto",      "procesamiento_lenguaje_natural.clasificacion_texto"),
            ("Topic Modeling (LDA)",        "procesamiento_lenguaje_natural.topic_modeling"),
        ],
    },
}


def limpiar():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def elegir(opciones, titulo):
    """Muestra una lista numerada y devuelve el índice elegido, o -1 para volver."""
    while True:
        print(f"\n{titulo}")
        print("-" * len(titulo))
        for i, op in enumerate(opciones, 1):
            print(f"  {i}. {op}")
        print("  0. Volver")
        try:
            sel = int(input("\n> "))
            if sel == 0:
                return -1
            if 1 <= sel <= len(opciones):
                return sel - 1
        except ValueError:
            pass
        print("Opción inválida.")


def ejecutar_modulo(ruta):
    try:
        mod = importlib.import_module(ruta)
        if hasattr(mod, "run"):
            print()
            mod.run()
        else:
            print(f"\nEste módulo aún no tiene función run().")
    except ImportError as e:
        print(f"\nNo se pudo importar el módulo: {e}")
    except Exception as e:
        print(f"\nError al ejecutar: {e}")
    input("\nEnter para continuar...")


def menu_metodos(metodos, titulo):
    nombres = [m[0] for m in metodos]
    while True:
        idx = elegir(nombres, titulo)
        if idx == -1:
            return
        nombre, ruta = metodos[idx]
        limpiar()
        print(f"  {nombre}")
        ejecutar_modulo(ruta)
        limpiar()


def menu_subcategorias(subcats, titulo):
    nombres = list(subcats.keys())
    while True:
        idx = elegir(nombres, titulo)
        if idx == -1:
            return
        nombre = nombres[idx]
        limpiar()
        menu_metodos(subcats[nombre], nombre)
        limpiar()


def main():
    categorias = list(MENU.keys())
    while True:
        limpiar()
        print("MATH ENGINE")
        idx = elegir(categorias, "Selecciona una categoría:")
        if idx == -1:
            print("\nHasta luego.")
            break
        nombre = categorias[idx]
        limpiar()
        menu_subcategorias(MENU[nombre], nombre)


if __name__ == "__main__":
    main()
