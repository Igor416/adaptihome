interface SideTextProps {
  text: string,
  marginTop?: number,
  marginRight?: number,
  marginBottom?: number,
  marginLeft?: number,
}

export default function SideText({text, marginTop = 10, marginRight = 20, marginBottom = 10, marginLeft = 20}: SideTextProps) {
  return <span style={{margin: `${marginTop}vh ${marginRight}vw ${marginBottom}vh ${marginLeft}vw`}} className='h4'>{text}</span>
}