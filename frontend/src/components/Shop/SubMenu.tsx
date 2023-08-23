import { ReactNode } from 'react'
import { Scrollbars } from 'react-custom-scrollbars-2';

interface SubMenuProps {
  active: boolean,
  side: 'left' | 'right',
  children: ReactNode[] | ReactNode,
  t?: (val: string) => string,
  clear?: () => void
}

export default function Submenu({active, side, children, t, clear}: SubMenuProps) {
  const menu = document.getElementById('shop_menu')
  const offset = Number(menu?.offsetTop) + Number(menu?.offsetHeight)
  return <div style={{
    zIndex: active ? 1100 : -1,
    marginTop: offset + 'px',
    height: `calc(100vh - ${offset}px)`,
    opacity: active ? 1 : 0,
  }} className={'d-flex pt-5 position-absolute bg-white transition-l top-0 w-50 ' + (side === 'left' ? 'start-0' : 'end-0')}>
    {side === 'left' && <div className='col-6'></div>}
    <Scrollbars style={{ width: 'calc(100% - 20px)', height: `calc(100vh - ${offset}px - 6.5rem)` }}>
      <div className={'position-relative col-6 flex-column text-start' + (side === 'right' ? ' ps-5' : '')}>{children}</div>
    </Scrollbars>
    {t && clear && <div onClick={clear} className='position-absolute w-100 px-5 py-3 bottom-0 bg-dark text-white text-start h4'>
      {t('clear')}
    </div>}
  </div>
}