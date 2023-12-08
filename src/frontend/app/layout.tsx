export const metadata = {
  title: 'Naviguide',
  description: 'Sistema de auxilio e navegação pelo almoxarifado da Ambev.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
