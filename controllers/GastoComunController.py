from services.GastoComunService import GastoComunService

class GastoComunController:
    @staticmethod
    def get_all_gasto_comun():
        return GastoComunService.get_all_gasto_comun()
    
    @staticmethod
    def create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo):
        return GastoComunService.create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo)
    
    @staticmethod
    def get_gasto_comun_by_id(gasto_comun_id):
        return GastoComunService.get_gasto_comun_by_id(gasto_comun_id)
    
    @staticmethod
    def registrar_pago(gasto_comun_id):
        return GastoComunService.update_gasto_comun(gasto_comun_id)
    
    @staticmethod
    def delete_gasto_comun(gasto_comun_id):
        return GastoComunService.delete_gasto_comun(gasto_comun_id)