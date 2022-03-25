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
                                <div className="social-links__item" id="bx_2970353375_1">
                                    <a className="social-links__link" href="https://www.instagram.com/kazandigitalweek/" target="_blank">
                                        <svg id="instagram_6_" data-name="instagram (6)" xmlns="http://www.w3.org/2000/svg" width="18.844" height="18.844" viewBox="0 0 18.844 18.844"><path id="Path_6236" data-name="Path 6236" d="M16.084,0H2.76A2.764,2.764,0,0,0,0,2.76V16.084a2.764,2.764,0,0,0,2.76,2.76H16.084a2.764,2.764,0,0,0,2.76-2.76V2.76A2.764,2.764,0,0,0,16.084,0ZM9.459,14.354a4.969,4.969,0,1,1,4.969-4.969A4.974,4.974,0,0,1,9.459,14.354ZM14.98,5.521a1.656,1.656,0,1,1,1.656-1.656A1.658,1.658,0,0,1,14.98,5.521Zm0,0"></path><path id="Path_6237" data-name="Path 6237" d="M392.552,90a.552.552,0,1,0,.552.552A.552.552,0,0,0,392.552,90Zm0,0" transform="translate(-377.572 -86.688)"></path><path id="Path_6238" data-name="Path 6238" d="M155.32,150a3.32,3.32,0,1,0,3.32,3.32A3.324,3.324,0,0,0,155.32,150Zm0,0" transform="translate(-145.861 -143.935)"></path></svg>                        </a>
                                </div>
                                <div className="social-links__item" id="bx_2970353375_2">
                                    <a className="social-links__link" href="https://twitter.com/digitalweek2020" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="23.195" height="18.846" viewBox="0 0 23.195 18.846"><path id="twitter_7_" data-name="twitter (7)" d="M23.2,50.231a9.914,9.914,0,0,1-2.74.751,4.729,4.729,0,0,0,2.092-2.628A9.5,9.5,0,0,1,19.532,49.5a4.755,4.755,0,0,0-8.226,3.252,4.9,4.9,0,0,0,.11,1.084,13.46,13.46,0,0,1-9.8-4.974,4.757,4.757,0,0,0,1.461,6.356,4.7,4.7,0,0,1-2.148-.586v.052a4.777,4.777,0,0,0,3.81,4.672,4.746,4.746,0,0,1-1.247.157,4.2,4.2,0,0,1-.9-.081,4.8,4.8,0,0,0,4.443,3.313,9.555,9.555,0,0,1-5.9,2.028A8.906,8.906,0,0,1,0,64.712a13.387,13.387,0,0,0,7.295,2.134A13.441,13.441,0,0,0,20.829,53.315c0-.21-.007-.413-.017-.615A9.486,9.486,0,0,0,23.2,50.231Z" transform="translate(0 -48)"></path></svg>                        </a>
                                </div>
                                <div className="social-links__item" id="bx_2970353375_3">
                                    <a className="social-links__link" href="https://vk.com/kazandigitalweek" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="23.391" height="13.645" viewBox="0 0 23.391 13.645"><path id="vk_4_" data-name="vk (4)" d="M19.41,12.824c-.378-.478-.27-.69,0-1.117,0,0,3.127-4.319,3.448-5.782h0c.16-.533,0-.925-.773-.925H19.53a1.1,1.1,0,0,0-1.112.712,20.919,20.919,0,0,1-3.144,5.137c-.595.584-.869.771-1.194.771-.16,0-.408-.187-.408-.72V5.925c0-.639-.182-.925-.721-.925H8.929a.612.612,0,0,0-.651.576c0,.606.921.746,1.017,2.451v3.7c0,.811-.147.96-.474.96-.869,0-2.979-3.13-4.23-6.711C4.338,5.282,4.092,5,3.436,5H.877C.147,5,0,5.337,0,5.713c0,.665.869,3.97,4.043,8.336,2.115,2.98,5.093,4.6,7.8,4.6,1.629,0,1.827-.359,1.827-.976,0-2.848-.147-3.117.669-3.117.378,0,1.029.187,2.55,1.625,1.738,1.7,2.023,2.468,3,2.468h2.557c.729,0,1.1-.359.886-1.066C22.845,16.09,19.558,13.029,19.41,12.824Z" transform="translate(0 -5)"></path></svg>                        </a>
                                </div>
                                <div className="social-links__item" id="bx_2970353375_5">
                                    <a className="social-links__link" href="https://www.facebook.com/KazanDigitalWeek" target="_blank">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 19 19"><path id="facebook_5_" data-name="facebook (5)" d="M16.217,0H2.783A2.787,2.787,0,0,0,0,2.783V16.217A2.787,2.787,0,0,0,2.783,19h5.6V12.283H6.16V8.943H8.387V6.68a3.343,3.343,0,0,1,3.34-3.34H15.1V6.68H11.727V8.943H15.1l-.557,3.34h-2.82V19h4.49A2.787,2.787,0,0,0,19,16.217V2.783A2.787,2.787,0,0,0,16.217,0Zm0,0"></path></svg>                        </a>
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
