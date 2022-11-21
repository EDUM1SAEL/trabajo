Public Class Form1
    Dim fraseOriginal, fraseEncriptada, frasedesencriptada As String
    Dim longitud, i As Integer
    Dim par As String
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        fraseOriginal = TextBoxTexto.Text
        frasedesencriptada = Nothing
        longitud = fraseOriginal.Length
        For i = 1 To longitud Step 2
            par = Mid(fraseOriginal, i, 2).ToString
            frasedesencriptada &= Chr(par).ToString


        Next
        TextBoxcifrado.Text = frasedesencriptada



    End Sub

    Private Sub ButtonCifrar_Click(sender As Object, e As EventArgs) Handles ButtonCifrar.Click
        fraseOriginal = UCase(TextBoxTexto.Text)
        fraseEncriptada = Nothing

        For Each item In fraseOriginal
            fraseEncriptada &= Asc(item.ToString)
        Next

        TextBoxcifrado.Text = fraseEncriptada

    End Sub
End Class
