from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class PDF:
    @staticmethod
    def gerar_pdf(nome_arquivo: str, pedidos: list, faturamento_total: float) -> bool:
        try:
            canva = canvas.Canvas(nome_arquivo, pagesize=A4)
            largura, altura = A4
            x = 30
            y = altura - 50

            canva.setFont("Helvetica-Bold", 16)
            canva.drawCentredString(largura/2, y, "Pizza Mais - Relatório Geral")
            y -= 10
            canva.line(x, y, largura - 30, y)
            y -= 30

            for pedido in pedidos:
                itens_validos = [item for item in pedido["itens"] if item[0] is not None]
                altura_caixa = 20 + 15 + (len(itens_validos) * 27) + 20

                if y - altura_caixa < 50:
                    canva.showPage()
                    y = altura - 50

                canva.setStrokeColor(colors.grey)
                canva.setLineWidth(0.3)
                canva.rect(x - 5, y + 15, largura - 60, -altura_caixa, stroke=1, fill=0)

                canva.setFont("Helvetica-Bold", 12)
                canva.drawString(x, y, f"Pedido #{pedido['id']}")
                canva.drawRightString(largura - 40, y, f"Data: {pedido['data']}")
                y -= 15

                canva.setFont("Helvetica-Bold", 10)
                canva.drawString(x + 10, y, "Itens:")
                y -= 15

                canva.setFont("Helvetica", 10)
                for nome, preco, tipo, descricao in itens_validos:
                    canva.drawString(x + 20, y, f"- {nome} ({tipo}) - R$ {preco:.2f}")
                    y -= 12
                    canva.setFillColor(colors.grey)
                    canva.drawString(x + 30, y, descricao)
                    canva.setFillColor(colors.black)
                    y -= 15

                canva.setFont("Helvetica-Bold", 11)
                canva.drawRightString(largura - 40, y, f"Total: R$ {pedido['valor']:.2f}")
                y -= 20

            if y <= 60:
                canva.showPage()
                y = altura - 60

            canva.line(x, y, largura - 30, y)
            y -= 25

            canva.setFont("Helvetica-Bold", 12)
            canva.drawCentredString(largura / 2, y, f"Faturamento Total: R$ {faturamento_total:.2f}")
            canva.save()
            return True

        except Exception as e:
            print(f"Erro ao salvar PDF: {e}")
            return False
