import logo from '../../logo.png' // relative path to image 

function Header() {
    return (
        <div>
            <header className="header">
                <div className="container">
                    <div className="d-md-flex">{/* style="justify-content: space-between;">*/}
                        <div className="d-md-flex">
                            <div className="header__left">
                                <picture>
                                    <img className="logo" src={logo} alt="" />
                                </picture>
                            </div>
                            <div className="mx-md-5 my-md-0 my-5">
                                <h1 className="heading heading_level-1 heading_white index-promo__heading">Международный форум<br /> Kazan Digital Week 2022</h1>
                            </div>
                        </div>
                        <div className="header__right lang">
                            <div className="social-links">
                                <div className="social-links__item" id="bx_2970353375_3">
                                    <a className="social-links__link" href="https://vk.com/kazandigitalweek" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="23.391" height="13.645" viewBox="0 0 23.391 13.645"><path id="vk_4_" data-name="vk (4)" d="M19.41,12.824c-.378-.478-.27-.69,0-1.117,0,0,3.127-4.319,3.448-5.782h0c.16-.533,0-.925-.773-.925H19.53a1.1,1.1,0,0,0-1.112.712,20.919,20.919,0,0,1-3.144,5.137c-.595.584-.869.771-1.194.771-.16,0-.408-.187-.408-.72V5.925c0-.639-.182-.925-.721-.925H8.929a.612.612,0,0,0-.651.576c0,.606.921.746,1.017,2.451v3.7c0,.811-.147.96-.474.96-.869,0-2.979-3.13-4.23-6.711C4.338,5.282,4.092,5,3.436,5H.877C.147,5,0,5.337,0,5.713c0,.665.869,3.97,4.043,8.336,2.115,2.98,5.093,4.6,7.8,4.6,1.629,0,1.827-.359,1.827-.976,0-2.848-.147-3.117.669-3.117.378,0,1.029.187,2.55,1.625,1.738,1.7,2.023,2.468,3,2.468h2.557c.729,0,1.1-.359.886-1.066C22.845,16.09,19.558,13.029,19.41,12.824Z" transform="translate(0 -5)"></path></svg>                        </a>
                                </div>
                                <div className="social-links__item" id="bx_2970353375_5">
                                    <a className="social-links__link" href="" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-telegram m-0" viewBox="0 0 16 16">
                                            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z" />
                                        </svg>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    );
}

export default Header;
