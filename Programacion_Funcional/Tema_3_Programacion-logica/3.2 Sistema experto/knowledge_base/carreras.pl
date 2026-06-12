% ==========================================
% HECHOS: Perfiles e Intereses por Carrera
% ==========================================

% Sistemas Computacionales
tiene_interes(sistemas_computacionales, programacion).
tiene_interes(sistemas_computacionales, redes).
tiene_interes(sistemas_computacionales, desarrollo_software).

% Ciencia de Datos
tiene_interes(ciencia_datos, matematicas).
tiene_interes(ciencia_datos, estadistica).
tiene_interes(ciencia_datos, analisis_datos).

% Administracion
tiene_interes(administracion, liderazgo).
tiene_interes(administracion, finanzas).
tiene_interes(administracion, organizacion).

% Industrial
tiene_interes(industrial, procesos).
tiene_interes(industrial, logistica).
tiene_interes(industrial, optimizacion).

% Alimentarias
tiene_interes(alimentarias, quimica).
tiene_interes(alimentarias, control_calidad).
tiene_interes(alimentarias, biologia).

% Desarrollo Comunitario
tiene_interes(desarrollo_comunitario, gestion_social).
tiene_interes(desarrollo_comunitario, proyectos_sostenibles).

% Gestion Empresarial
tiene_interes(gestion_empresarial, negocios).
tiene_interes(gestion_empresarial, innovacion).
tiene_interes(gestion_empresarial, estrategias).

% ==========================================
% REGLAS DE INFERENCIA
% ==========================================
% Una regla simple para empezar: sugiere una carrera si el alumno comparte un interes clave.
sugerir_por_interes(Carrera, InteresUsuario) :-
    tiene_interes(Carrera, InteresUsuario).