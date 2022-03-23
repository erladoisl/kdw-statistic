function testWebP(callback) {

var webP = new Image();
webP.onload = webP.onerror = function () {
callback(webP.height == 2);
};
webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
}

testWebP(function (support) {

if (support == true) {
document.querySelector('body').classList.add('webp');
}else{
document.querySelector('body').classList.add('no-webp');
}
});;
const content = {
  contentOne: {
    title: 'Цифровые технологии в образовании',
    description: `Цифровые технологии в образовании — это способ 
    организации современной образовательной среды, 
    основанный на цифровых технологиях. Внедрение 
    цифровых технологий в систему образования 
    обеспечивает развитие навыков владения цифровыми 
    технологиями, применение их в каждодневной 
    бытовой и рабочей обстановке.
    `
  },
  contentTwo: {
    title: 'Индустрия 4.0',
    description: `Индустрия 4.0– ведущий тренд происходящей на 
    наших глазах «Четвертой промышленной революции». 
    Характерные черты Индустрии 4.0 – это полностью 
    автоматизированные производства, на которых 
    управление всеми процессами осуществляется 
    в режиме реального времени и с учетом меняющихся 
    внешних условий.`
  },
  contentThree: {
    title: 'Экосистема Финтех',
    description: `Ветвь мероприятий, охватывающая актуальные 
    направления финансовых технологий для банковского 
    сегмента, законодательное регулирование финтех 
    проектов, применение технологий искусственного 
    интеллекта и роботизациии в банковской отрасли.`
  },
  contentFour: {
    title: 'Цифровые технологии в культуре',
    description: `Международная научно-практическая конференция 
    ITS Forum – Kazan, объединяющая различные 
    направления приложения компонентов 
    интеллектуальных транспортных систем и 
    ситуационных центров к решению актуальных задач 
    обеспечения безопасности жизнедеятельности.`
  },
  contentFive: {
    title: 'Цифровые технологии в сфере государственного управления',
    description: ``
  },
  contentSix: {
    title: 'Цифровые технологии в сфере сельского хозяйства',
    description: `Обмен опытом в формировании отраслевых платформ для развития и цифровизации агропромышленного комплекса в регионах
    Опыт преодоления научно-технических, организационных и правовых проблем цифровизации сельскохозяйственных сегментов, формирования и использования данных, корпоративных информационных и вычислительных ресурсов.
    Разработки и практические результаты использования региональными агрокомплексами систем геоинформационного мониторинга агропромышленного производства, интеллектуальных роботизированных средств, систем принятия решений на основе больших данных.
    Обмен опытом по укомплектованию агропромышленного комплекса специалистами с цифровыми компетенциями.
    Методы и учебные программы, ориентированные на сельскохозяйственный сектор экономики. Опыт работы учебных центров с привлечением преподавателей, оборудования, цифровых инструментов и вычислительных ресурсов образовательных частных компаний.
    Готовые к масштабированию практики создания и эксплуатации роботизированных платформ и комплексов в животноводстве, растениеводстве на закрытых почвах и экосистемах фитотронов с использованием технологий искусственного интеллекта.`
  },
  contentSeven: {
    title: 'Интеллектуальные транспортные системы',
    description: `Международная научно-практическая конференция 
    ITS Forum – Kazan, объединяющая различные 
    направления приложения компонентов 
    интеллектуальных транспортных систем и 
    ситуационных центров к решению актуальных задач 
    обеспечения безопасности жизнедеятельности.`
  },
  contentEight: {
    title: 'Инновации, интегрированные в бизнес',
    description: `Тематическое направление, включающее в себя 
    трендовые идеи на стыке корпоративных задач и 
    стартапов, мировые и российские тенденции 
    венчурного инвестирования, инновационные идеи 
    молодых компаний, направленные на трансформацию 
    устоявшихся бизнес-процессов.`
  },
  contentNine: {
    title: 'Кибербезопасность',
    description: `Направление, включающее подробный обзор мировых 
    и российских трендов в этой сфере: технических 
    средств защиты информации, отраслевых аспектов 
    обеспечения кибербезопасности, практик применения 
    сервисов кибербезопасности, регулирующего 
    законодательства в области защиты информации.`
  },
  contentTen: {
    title: 'Цифровые технологии в здравоохранении',
    description: `Цифровая медицина является совершенно новым 
    форматом здравоохранения. Практическая реализация 
    цифровых технологий в области медицины набрала 
    высокий темп. Она представляет собой необходимый 
    набор программного и аппаратного обеспечения для 
    взаимодействия пациента и доктора и возможности 
    дистанционного исследования важнейших 
    характеристик здоровья человека.`
  }
};

function showModal(event) {
  if (event) {
    const modalWindow = document.getElementById('modal');
    const wrapper = document.getElementById('wrapper');
    const title = modalWindow.querySelector('.modal__title > p');
    const description = modalWindow.querySelector('.modal__description > p');
    
    title.textContent = content[event.name].title;
    description.textContent = content[event.name].description;
    modalWindow.style.top = '50%';
    modalWindow.style.zIndex = '9999';
    modalWindow.style.opacity = '1';

    wrapper.style.overflow = 'hidden'
  }
}

function hideModal() {
  const modalWindow = document.getElementById('modal');
  const wrapper = document.getElementById('wrapper');

  modalWindow.style.zIndex = '-1';
  modalWindow.style.top = '-100%';
  modalWindow.style.opacity = '0';

  wrapper.style.overflow = 'auto'

}

function showModalInfo() {
  const modalWindow = document.getElementById('modal-info');
  modalWindow.style.top = '50%';
  modalWindow.style.zIndex = '9999';
  modalWindow.style.opacity = '1';
}

function hideModalInfo() {
  const modalWindow = document.getElementById('modal-info');
  modalWindow.style.zIndex = '-1';
  modalWindow.style.top = '-100%';
  modalWindow.style.opacity = '0';
}

function showModalVideo() {
  const modalWindow = document.getElementById('modal-video');
  const videoKDW = document.getElementById('video-kdw');
  modalWindow.style.top = '50%';
  modalWindow.style.zIndex = '9999';
  modalWindow.style.opacity = '1';
  videoKDW.play();
}
function hideModalVideo() {
  const modalWindow = document.getElementById('modal-video');
  const videoKDW = document.getElementById('video-kdw');
  modalWindow.style.zIndex = '-1';
  modalWindow.style.top = '-100%';
  modalWindow.style.opacity = '0';
  videoKDW.pause();
}
;


