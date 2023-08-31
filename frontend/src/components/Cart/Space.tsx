interface Space {
  color?: 'transparent' | 'white'
}

export default function Space({color = 'transparent'}) {
  return <div style={{width: '12.5%', flex: '0 0 auto'}} className={'bg-' + color}></div>
}